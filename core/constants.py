"""
Constantes globais do projeto Tutor Docente.
Define modelos de AI, configurações e valores padrão.
"""

from enum import Enum


class AIModels(str, Enum):
    """Modelos de AI disponíveis."""
    
    GEMINI_2_5_PRO = "gemini-2.5-pro"
    GEMINI_2_5_FLASH = "gemini-2.5-flash"
    GEMINI_2_5_FLASH_LITE = "gemini-2.5-flash-lite"
    GEMINI_2_0_FLASH = "gemini-2.0-flash"


class AgentConfig:
    """Configurações padrão dos agentes."""
    
    DEFAULT_MODEL = AIModels.GEMINI_2_5_FLASH
    ORCHESTRATOR_MODEL = AIModels.GEMINI_2_5_PRO
    FEEDBACK_MODEL = AIModels.GEMINI_2_5_PRO
    
    # Timeouts e limites
    MAX_RETRIES = 3
    TIMEOUT_SECONDS = 60


# Configurações de ambiente
ENV_GOOGLE_API_KEY = "GOOGLE_API_KEY"
ENV_FRONTEND_ORIGIN = "FRONTEND_ORIGIN"
