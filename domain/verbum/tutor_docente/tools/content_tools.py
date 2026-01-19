"""
Tools para carregar e gerenciar conteúdos das trilhas.
"""

from typing import Optional
from pathlib import Path
from functools import lru_cache

from google.adk.tools import ToolContext

from ..constants import STEP_CONFIGS, AVAILABLE_MATERIALS


# Caminho base dos conteúdos
CONTENT_BASE_PATH = Path(__file__).parent.parent / "content"


@lru_cache(maxsize=50)
def _load_content_file(trilho: str, filename: str) -> str:
    """Carrega um arquivo de conteúdo (com cache)."""
    filepath = CONTENT_BASE_PATH / trilho / filename
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Conteúdo não encontrado: {trilho}/{filename}]"


def get_step_content(step_id: str, tool_context: ToolContext = None) -> str:
    """
    Carrega o conteúdo associado a um step.
    
    Args:
        step_id: ID do step
        tool_context: Contexto da ferramenta (acesso ao estado)
    
    Returns:
        Conteúdo do arquivo associado ao step, ou string vazia se não houver.
    """
    config = STEP_CONFIGS.get(step_id)
    if not config or not config.content_file:
        return ""
    
    return _load_content_file("trilho01", config.content_file)


def get_content_by_filename(trilho: str, filename: str, tool_context: ToolContext = None) -> str:
    """
    Carrega um conteúdo específico por nome de arquivo.
    
    Args:
        trilho: ID do trilho (ex: "trilho01")
        filename: Nome do arquivo (ex: "apresentacao.md")
        tool_context: Contexto da ferramenta
    
    Returns:
        Conteúdo do arquivo.
    """
    if filename not in AVAILABLE_MATERIALS:
        return f"[Material não disponível: {filename}]"
    
    return _load_content_file(trilho, filename)


def get_available_content_files(trilho: str = "trilho01", tool_context: ToolContext = None) -> list[str]:
    """
    Lista os arquivos de conteúdo disponíveis para um trilho.
    
    Args:
        trilho: ID do trilho
        tool_context: Contexto da ferramenta
    
    Returns:
        Lista de nomes de arquivos disponíveis.
    """
    trilho_path = CONTENT_BASE_PATH / trilho
    if not trilho_path.exists():
        return []
    
    return [f.name for f in trilho_path.glob("*.md")]


def get_video03_content(caminho: str, tool_context: ToolContext = None) -> str:
    """
    Carrega o conteúdo do vídeo 03 baseado no caminho escolhido.
    
    Args:
        caminho: "A" para Inclusão Solidária ou "B" para Protagonismo Ativo
        tool_context: Contexto da ferramenta
    
    Returns:
        Conteúdo do arquivo de vídeo correspondente.
    """
    if caminho == "A":
        return _load_content_file("trilho01", "video03_inclusao_solidaria.md")
    elif caminho == "B":
        return _load_content_file("trilho01", "video03_protagonismo_ativo.md")
    else:
        return "[Caminho inválido. Escolha A ou B.]"


def validate_material_reference(material_name: str) -> bool:
    """
    Valida se uma referência a material está autorizada.
    
    Args:
        material_name: Nome do material mencionado
    
    Returns:
        True se o material está na lista de materiais disponíveis.
    """
    # Normalizar o nome
    normalized = material_name.lower().strip()
    
    # Verificar contra lista de materiais
    for material in AVAILABLE_MATERIALS:
        if normalized in material.lower():
            return True
    
    # Materiais proibidos (exemplos mencionados na política)
    forbidden = [
        "coragem de educar",
        "teoria do iceberg",
    ]
    
    for forbidden_item in forbidden:
        if forbidden_item in normalized:
            return False
    
    return False
