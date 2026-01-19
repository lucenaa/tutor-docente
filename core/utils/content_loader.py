"""
Utilitário para carregar conteúdos das trilhas (.md files).
"""

import os
from pathlib import Path
from functools import lru_cache

from core.exceptions import ContentNotFoundError


class ContentLoader:
    """Carregador de conteúdos das trilhas."""
    
    def __init__(self, base_path: str | Path | None = None):
        """
        Inicializa o loader com o caminho base dos conteúdos.
        
        Args:
            base_path: Caminho base para os conteúdos. Se None, usa o padrão.
        """
        if base_path is None:
            # Padrão: domain/verbum/tutor_docente/content
            base_path = Path(__file__).parent.parent.parent / "domain" / "verbum" / "tutor_docente" / "content"
        
        self.base_path = Path(base_path)
    
    def load(self, trilho: str, filename: str) -> str:
        """
        Carrega o conteúdo de um arquivo markdown.
        
        Args:
            trilho: ID do trilho (ex: "trilho01")
            filename: Nome do arquivo (ex: "apresentacao.md")
        
        Returns:
            Conteúdo do arquivo como string.
        
        Raises:
            ContentNotFoundError: Se o arquivo não for encontrado.
        """
        filepath = self.base_path / trilho / filename
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise ContentNotFoundError(f"{trilho}/{filename}")
    
    def load_safe(self, trilho: str, filename: str, default: str = "") -> str:
        """
        Carrega o conteúdo de forma segura, retornando default se não encontrar.
        
        Args:
            trilho: ID do trilho
            filename: Nome do arquivo
            default: Valor padrão se não encontrar
        
        Returns:
            Conteúdo do arquivo ou valor padrão.
        """
        try:
            return self.load(trilho, filename)
        except ContentNotFoundError:
            return default
    
    def exists(self, trilho: str, filename: str) -> bool:
        """Verifica se um arquivo de conteúdo existe."""
        filepath = self.base_path / trilho / filename
        return filepath.exists()
    
    def list_files(self, trilho: str) -> list[str]:
        """Lista todos os arquivos de conteúdo de um trilho."""
        trilho_path = self.base_path / trilho
        if not trilho_path.exists():
            return []
        return [f.name for f in trilho_path.glob("*.md")]


# Instância global do loader
_default_loader: ContentLoader | None = None


def get_content_loader() -> ContentLoader:
    """Retorna a instância global do ContentLoader."""
    global _default_loader
    if _default_loader is None:
        _default_loader = ContentLoader()
    return _default_loader


@lru_cache(maxsize=100)
def load_content(trilho: str, filename: str) -> str:
    """
    Função de conveniência para carregar conteúdo com cache.
    
    Args:
        trilho: ID do trilho (ex: "trilho01")
        filename: Nome do arquivo (ex: "apresentacao.md")
    
    Returns:
        Conteúdo do arquivo.
    """
    return get_content_loader().load(trilho, filename)
