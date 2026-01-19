"""
Entry point principal do Tutor Docente.
Carrega o agente via factory baseado na variável de ambiente ADK_ENTRYPOINT.
"""

import os
from agent_factories import get_agent_by_name, AgentType

# Obter o tipo de agente da variável de ambiente
# Default: tutor_docente
AGENT_ENTRYPOINT = os.environ.get("ADK_ENTRYPOINT", "tutor_docente")

# Carregar o agente
root_agent = get_agent_by_name(AGENT_ENTRYPOINT)

# Exportar para o ADK
__all__ = ["root_agent"]
