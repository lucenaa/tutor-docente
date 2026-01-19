"""
Agent Factories - Factory pattern para instanciar agentes.
"""

from enum import Enum
from typing import Dict, Callable, Any


class AgentType(Enum):
    """Tipos de agentes disponíveis."""
    TUTOR_DOCENTE = "tutor_docente"


def _get_tutor_docente_agent():
    """Factory para o agente Tutor Docente."""
    from domain.verbum.tutor_docente.agent import root_agent
    return root_agent


# Mapa de factories
AGENT_FACTORY_MAP: Dict[AgentType, Callable[[], Any]] = {
    AgentType.TUTOR_DOCENTE: _get_tutor_docente_agent,
}


def get_agent(agent_type: AgentType):
    """
    Obtém uma instância de agente pelo tipo.
    
    Args:
        agent_type: Tipo do agente
    
    Returns:
        Instância do agente
    
    Raises:
        ValueError: Se o tipo de agente não for encontrado
    """
    factory = AGENT_FACTORY_MAP.get(agent_type)
    if not factory:
        raise ValueError(f"Tipo de agente não encontrado: {agent_type}")
    return factory()


def get_agent_by_name(name: str):
    """
    Obtém uma instância de agente pelo nome.
    
    Args:
        name: Nome do agente (ex: "tutor_docente")
    
    Returns:
        Instância do agente
    """
    try:
        agent_type = AgentType(name)
        return get_agent(agent_type)
    except ValueError:
        raise ValueError(f"Agente não encontrado: {name}. Disponíveis: {[t.value for t in AgentType]}")
