"""
Tools para manipular o estado da sessão.
"""

from typing import Optional, Literal
from google.adk.tools import ToolContext

from ..constants import (
    TRILHO01_STEPS_ORDER,
    get_next_step as _get_next_step,
    is_valid_step,
)
from ..types import FeedbackLevel


def get_current_step(tool_context: ToolContext) -> str:
    """
    Retorna o step atual da sessão.
    
    Args:
        tool_context: Contexto da ferramenta
    
    Returns:
        ID do step atual.
    """
    return tool_context.state.get("current_step", TRILHO01_STEPS_ORDER[0])


def get_completed_steps(tool_context: ToolContext) -> list[str]:
    """
    Retorna a lista de steps completados.
    
    Args:
        tool_context: Contexto da ferramenta
    
    Returns:
        Lista de IDs de steps completados.
    """
    return tool_context.state.get("completed_steps", [])


def mark_step_completed(step_id: str, tool_context: ToolContext) -> bool:
    """
    Marca um step como completado.
    
    Args:
        step_id: ID do step a marcar
        tool_context: Contexto da ferramenta
    
    Returns:
        True se o step foi marcado com sucesso.
    """
    if not is_valid_step(step_id):
        return False
    
    completed = tool_context.state.get("completed_steps", [])
    if step_id not in completed:
        completed.append(step_id)
        tool_context.state["completed_steps"] = completed
    
    return True


def advance_to_next_step(tool_context: ToolContext) -> Optional[str]:
    """
    Avança para o próximo step na sequência.
    
    Args:
        tool_context: Contexto da ferramenta
    
    Returns:
        ID do próximo step, ou None se for o último.
    """
    current = get_current_step(tool_context)
    
    # Marcar atual como completado
    mark_step_completed(current, tool_context)
    
    # Obter próximo
    next_step = _get_next_step(current)
    
    if next_step:
        tool_context.state["current_step"] = next_step
        return next_step
    else:
        # Último step - marcar lição como completada
        tool_context.state["lesson_completed"] = True
        return None


def set_path_choice(choice: Literal["A", "B"], tool_context: ToolContext) -> bool:
    """
    Define a escolha de caminho do docente.
    
    Args:
        choice: "A" para Inclusão Solidária ou "B" para Protagonismo Ativo
        tool_context: Contexto da ferramenta
    
    Returns:
        True se a escolha foi registrada.
    """
    if choice not in ["A", "B"]:
        return False
    
    tool_context.state["caminho_escolhido"] = choice
    return True


def get_path_choice(tool_context: ToolContext) -> Optional[str]:
    """
    Retorna a escolha de caminho do docente.
    
    Args:
        tool_context: Contexto da ferramenta
    
    Returns:
        "A", "B" ou None se ainda não escolheu.
    """
    return tool_context.state.get("caminho_escolhido")


def is_lesson_completed(tool_context: ToolContext) -> bool:
    """
    Verifica se a lição foi completada.
    
    Args:
        tool_context: Contexto da ferramenta
    
    Returns:
        True se a lição está completa.
    """
    return tool_context.state.get("lesson_completed", False)


def is_step_completed(step_id: str, tool_context: ToolContext) -> bool:
    """
    Verifica se um step específico foi completado.
    
    Args:
        step_id: ID do step
        tool_context: Contexto da ferramenta
    
    Returns:
        True se o step está completo.
    """
    completed = get_completed_steps(tool_context)
    return step_id in completed


def record_internal_evaluation(
    step_id: str,
    evaluation: FeedbackLevel,
    tool_context: ToolContext
) -> None:
    """
    Registra uma avaliação interna da resposta do docente.
    
    Args:
        step_id: ID do step
        evaluation: Nível de feedback
        tool_context: Contexto da ferramenta
    """
    evaluations = tool_context.state.get("internal_evaluations", {})
    evaluations[step_id] = evaluation.value
    tool_context.state["internal_evaluations"] = evaluations


def get_internal_evaluation(step_id: str, tool_context: ToolContext) -> Optional[FeedbackLevel]:
    """
    Recupera a avaliação interna de um step.
    
    Args:
        step_id: ID do step
        tool_context: Contexto da ferramenta
    
    Returns:
        Nível de feedback ou None.
    """
    evaluations = tool_context.state.get("internal_evaluations", {})
    value = evaluations.get(step_id)
    if value:
        return FeedbackLevel(value)
    return None


def set_docente_etapa(etapa: str, tool_context: ToolContext) -> None:
    """
    Define a etapa de ensino do docente.
    
    Args:
        etapa: "Anos Iniciais", "Educação Infantil", etc.
        tool_context: Contexto da ferramenta
    """
    tool_context.state["etapa_docente"] = etapa


def get_docente_etapa(tool_context: ToolContext) -> Optional[str]:
    """
    Retorna a etapa de ensino do docente.
    
    Args:
        tool_context: Contexto da ferramenta
    
    Returns:
        Etapa de ensino ou None.
    """
    return tool_context.state.get("etapa_docente")


def detect_path_choice_from_message(message: str) -> Optional[Literal["A", "B"]]:
    """
    Detecta a escolha de caminho a partir da mensagem do usuário.
    
    Args:
        message: Mensagem do usuário
    
    Returns:
        "A", "B" ou None se não detectou escolha.
    """
    msg = message.strip().upper()
    
    # Detecção direta
    if msg in ["A", "CAMINHO A", "OPÇÃO A", "ESCOLHO A", "A)"]:
        return "A"
    if msg in ["B", "CAMINHO B", "OPÇÃO B", "ESCOLHO B", "B)"]:
        return "B"
    
    # Detecção por palavras-chave
    msg_lower = message.lower()
    if "inclusão solidária" in msg_lower or "inclusao solidaria" in msg_lower:
        return "A"
    if "protagonismo ativo" in msg_lower:
        return "B"
    
    return None


def detect_ready_to_advance(message: str) -> bool:
    """
    Detecta se o usuário está pronto para avançar para a próxima etapa.
    
    Args:
        message: Mensagem do usuário
    
    Returns:
        True se detectou intenção de avançar.
    """
    msg = message.lower().strip()
    
    ready_keywords = [
        "sim", "pode prosseguir", "continuar", "próxima etapa", "sem dúvidas",
        "pode seguir", "vamos em frente", "ok", "tudo certo", "pode continuar",
        "sem dúvida", "pode avançar", "vamos", "próximo", "próxima", "seguir",
        "prosseguir", "avançar"
    ]
    
    return any(keyword in msg for keyword in ready_keywords)
