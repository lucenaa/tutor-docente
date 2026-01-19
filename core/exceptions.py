"""
Exceções customizadas do Tutor Docente.
"""


class TutorDocenteError(Exception):
    """Exceção base para erros do Tutor Docente."""
    
    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}


class StepNotFoundError(TutorDocenteError):
    """Exceção quando um step não é encontrado."""
    
    def __init__(self, step_id: str):
        super().__init__(
            f"Step não encontrado: {step_id}",
            details={"step_id": step_id}
        )


class InvalidStateError(TutorDocenteError):
    """Exceção quando o estado da sessão é inválido."""
    
    def __init__(self, message: str, current_state: dict | None = None):
        super().__init__(
            message,
            details={"current_state": current_state or {}}
        )


class ContentNotFoundError(TutorDocenteError):
    """Exceção quando um conteúdo não é encontrado."""
    
    def __init__(self, filename: str):
        super().__init__(
            f"Conteúdo não encontrado: {filename}",
            details={"filename": filename}
        )


class InvalidPathChoiceError(TutorDocenteError):
    """Exceção quando a escolha de caminho é inválida."""
    
    def __init__(self, choice: str):
        super().__init__(
            f"Escolha de caminho inválida: {choice}. Esperado: 'A' ou 'B'",
            details={"choice": choice, "valid_choices": ["A", "B"]}
        )
