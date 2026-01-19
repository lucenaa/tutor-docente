"""
Script de deploy do Tutor Docente para Vertex AI.
"""

import os
import sys
from pathlib import Path

# Adicionar raiz ao path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def deploy_tutor_docente(update_existing: bool = True):
    """
    Deploy do agente Tutor Docente.
    
    Args:
        update_existing: Se deve atualizar agente existente ou criar novo
    """
    # Importar utilidades de deploy (quando disponíveis)
    try:
        from scripts.deployment_utils import (
            initialize_vertex_ai,
            create_deployment_app,
            deploy_or_update_agent,
            print_deployment_info
        )
    except ImportError:
        print("Utilitários de deploy não disponíveis.")
        print("Para deploy local, use: uv run adk web domain/verbum --port 8000")
        return None
    
    # Inicializar Vertex AI
    initialize_vertex_ai()
    
    # Carregar agente
    from agent_factories import AgentType, AGENT_FACTORY_MAP
    
    agent_type = AgentType.TUTOR_DOCENTE
    factory = AGENT_FACTORY_MAP[agent_type]
    root_agent = factory()
    
    # Nome do deploy
    base_name = os.environ.get("ADK_DISPLAY_NAME", "verbum-tutor-docente")
    
    # Variáveis de ambiente para o agente
    agent_env_vars = {
        "GOOGLE_API_KEY": os.environ.get("GOOGLE_API_KEY"),
    }
    agent_env_vars = {k: v for k, v in agent_env_vars.items() if v is not None}
    
    # Criar app de deploy
    app = create_deployment_app(root_agent, env_vars=agent_env_vars, enable_tracing=True)
    
    # Deploy
    remote_app = deploy_or_update_agent(app, base_name, update_existing=update_existing)
    
    # Info
    version = remote_app.display_name.split('-')[-1] if '-' in remote_app.display_name else "v1.0"
    is_update = update_existing
    
    print_deployment_info(version, remote_app.display_name, remote_app.resource_name, "tutor docente", is_update)
    
    return remote_app, version


if __name__ == "__main__":
    update_existing = os.environ.get("UPDATE_EXISTING", "true").lower() == "true"
    deploy_tutor_docente(update_existing=update_existing)
