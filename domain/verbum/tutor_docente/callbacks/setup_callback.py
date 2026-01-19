"""
Callbacks de setup e finalização da sessão.
"""

import logging
from google.adk.agents.callback_context import CallbackContext

from ..constants import TRILHO01_STEPS_ORDER

logger = logging.getLogger(__name__)


def setup_session_callback(callback_context: CallbackContext) -> None:
    """
    Callback executado ANTES do agente rodar.
    Inicializa o estado da sessão se necessário.
    """
    state = callback_context.session.state
    
    # Inicializar estado básico se não existir
    if "current_step" not in state:
        state["current_step"] = TRILHO01_STEPS_ORDER[0]
        logger.info(f"[TutorDocente] Sessão iniciada no step: {state['current_step']}")
    
    if "completed_steps" not in state:
        state["completed_steps"] = []
    
    if "lesson_completed" not in state:
        state["lesson_completed"] = False
    
    if "internal_evaluations" not in state:
        state["internal_evaluations"] = {}
    
    if "waiting_for_response" not in state:
        state["waiting_for_response"] = False
    
    # Extrair informação da mensagem do usuário se disponível
    _process_user_message(callback_context)


def after_agent_callback(callback_context: CallbackContext) -> None:
    """
    Callback executado DEPOIS do agente rodar.
    Limpa dados temporários e valida estado.
    """
    state = callback_context.session.state
    
    # Verificar se a lição foi completada
    if state.get("current_step") == TRILHO01_STEPS_ORDER[-1]:
        # Verificar se o step final está nos completados
        if TRILHO01_STEPS_ORDER[-1] in state.get("completed_steps", []):
            state["lesson_completed"] = True
            logger.info("[TutorDocente] Trilho 01 finalizado com sucesso!")
    
    # Log do estado atual para debug
    logger.debug(f"[TutorDocente] Estado atual: step={state.get('current_step')}, "
                 f"completed={len(state.get('completed_steps', []))}, "
                 f"caminho={state.get('caminho_escolhido')}")


def _process_user_message(callback_context: CallbackContext) -> None:
    """
    Processa a mensagem do usuário para extrair informações relevantes.
    """
    # Tentar extrair a última mensagem do usuário do contexto
    # Isso depende de como o ADK passa as mensagens
    
    # Por enquanto, apenas verificamos se há informações específicas no estado
    state = callback_context.session.state
    current_step = state.get("current_step", "")
    
    # Se estamos no step de escolha de caminho, verificar se há escolha pendente
    if current_step == "t01_s16_escolha_caminho":
        # A detecção da escolha será feita pelo orquestrador ou subagente
        pass
    
    # Se estamos no primeiro step, verificar se há etapa do docente
    if current_step == "t01_s1_intro":
        # A detecção da etapa será feita pelo subagente
        pass


def initialize_fresh_session(callback_context: CallbackContext) -> None:
    """
    Inicializa uma sessão completamente nova.
    Útil para reiniciar a trilha.
    """
    state = callback_context.session.state
    
    # Limpar todo o estado
    state.clear()
    
    # Reinicializar com valores padrão
    state["current_step"] = TRILHO01_STEPS_ORDER[0]
    state["completed_steps"] = []
    state["lesson_completed"] = False
    state["internal_evaluations"] = {}
    state["waiting_for_response"] = False
    state["caminho_escolhido"] = None
    state["etapa_docente"] = None
    
    logger.info("[TutorDocente] Sessão reinicializada")
