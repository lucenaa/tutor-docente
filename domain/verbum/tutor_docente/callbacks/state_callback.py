"""
Callbacks de gerenciamento de estado entre steps.
"""

import logging
from typing import Optional
from google.adk.agents.callback_context import CallbackContext

from ..constants import (
    TRILHO01_STEPS_ORDER,
    STEP_CONFIGS,
    get_next_step,
    get_rubric,
)
from ..types import StepType
from ..tools.content_tools import get_step_content

logger = logging.getLogger(__name__)


def before_step_callback(callback_context: CallbackContext) -> None:
    """
    Callback executado ANTES de processar um step.
    Prepara o contexto e carrega conteúdos necessários.
    """
    state = callback_context.session.state
    current_step = state.get("current_step", TRILHO01_STEPS_ORDER[0])
    
    # Obter configuração do step
    step_config = STEP_CONFIGS.get(current_step)
    if not step_config:
        logger.warning(f"[TutorDocente] Step não encontrado: {current_step}")
        return
    
    # Carregar conteúdo se houver arquivo associado
    if step_config.content_file:
        content = get_step_content(current_step)
        state["_current_content"] = content
        logger.debug(f"[TutorDocente] Conteúdo carregado para {current_step}")
    else:
        state["_current_content"] = ""
    
    # Carregar rubrica se for step de pergunta
    if step_config.type == StepType.QUESTION:
        rubric = get_rubric(current_step)
        if rubric:
            state["_current_rubric"] = rubric.model_dump()
            logger.debug(f"[TutorDocente] Rubrica carregada para {current_step}")
    
    # Preparar informações do step para o agente
    state["_step_type"] = step_config.type.value
    state["_step_has_question"] = step_config.has_question
    state["_step_question"] = step_config.question
    
    # Verificar se o step já foi completado
    completed_steps = state.get("completed_steps", [])
    state["_step_already_completed"] = current_step in completed_steps
    
    logger.info(f"[TutorDocente] Preparando step: {current_step} (tipo: {step_config.type.value})")


def after_step_callback(callback_context: CallbackContext) -> None:
    """
    Callback executado DEPOIS de processar um step.
    Atualiza estado e prepara transição.
    """
    state = callback_context.session.state
    current_step = state.get("current_step", "")
    
    # Limpar dados temporários do step
    temp_keys = [
        "_current_content",
        "_current_rubric",
        "_step_type",
        "_step_has_question",
        "_step_question",
        "_step_already_completed",
    ]
    for key in temp_keys:
        state.pop(key, None)
    
    logger.debug(f"[TutorDocente] Step {current_step} processado")


def prepare_next_step(callback_context: CallbackContext) -> Optional[str]:
    """
    Prepara a transição para o próximo step.
    
    Returns:
        ID do próximo step ou None se for o último.
    """
    state = callback_context.session.state
    current_step = state.get("current_step", "")
    
    # Marcar step atual como completado
    completed = state.get("completed_steps", [])
    if current_step not in completed:
        completed.append(current_step)
        state["completed_steps"] = completed
    
    # Obter próximo step
    next_step = get_next_step(current_step)
    
    if next_step:
        state["current_step"] = next_step
        logger.info(f"[TutorDocente] Avançando para: {next_step}")
        return next_step
    else:
        state["lesson_completed"] = True
        logger.info("[TutorDocente] Trilho finalizado!")
        return None


def should_advance_step(callback_context: CallbackContext, user_message: str) -> bool:
    """
    Verifica se deve avançar para o próximo step baseado na mensagem do usuário.
    
    Args:
        callback_context: Contexto do callback
        user_message: Mensagem do usuário
    
    Returns:
        True se deve avançar.
    """
    # Palavras que indicam que o usuário quer continuar
    advance_keywords = [
        "sim", "pode prosseguir", "continuar", "próxima", "próximo",
        "sem dúvidas", "pode seguir", "vamos", "ok", "tudo certo",
        "pode continuar", "avançar", "prosseguir", "seguir"
    ]
    
    msg_lower = user_message.lower().strip()
    return any(keyword in msg_lower for keyword in advance_keywords)


def handle_path_choice_detection(callback_context: CallbackContext, user_message: str) -> Optional[str]:
    """
    Detecta e registra a escolha de caminho do usuário.
    
    Args:
        callback_context: Contexto do callback
        user_message: Mensagem do usuário
    
    Returns:
        "A", "B" ou None se não detectou escolha.
    """
    state = callback_context.session.state
    current_step = state.get("current_step", "")
    
    # Só detecta no step de escolha de caminho
    if current_step != "t01_s16_escolha_caminho":
        return None
    
    msg = user_message.strip().upper()
    
    # Detecção direta
    if msg in ["A", "CAMINHO A", "OPÇÃO A", "ESCOLHO A"]:
        state["caminho_escolhido"] = "A"
        logger.info("[TutorDocente] Caminho escolhido: A (Inclusão Solidária)")
        return "A"
    
    if msg in ["B", "CAMINHO B", "OPÇÃO B", "ESCOLHO B"]:
        state["caminho_escolhido"] = "B"
        logger.info("[TutorDocente] Caminho escolhido: B (Protagonismo Ativo)")
        return "B"
    
    # Detecção por palavras-chave
    msg_lower = user_message.lower()
    if "inclusão solidária" in msg_lower or "inclusao solidaria" in msg_lower:
        state["caminho_escolhido"] = "A"
        return "A"
    
    if "protagonismo ativo" in msg_lower:
        state["caminho_escolhido"] = "B"
        return "B"
    
    return None
