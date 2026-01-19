"""
Tipos e Schemas Pydantic para o Tutor Docente.
Define estruturas de dados para estado, configuração e comunicação.
"""

from typing import Literal, Optional
from pydantic import BaseModel, Field
from enum import Enum


# ══════════════════════════════════════════════════════════════
# Enums
# ══════════════════════════════════════════════════════════════

class PathChoice(str, Enum):
    """Escolha de caminho no Trilho 01."""
    INCLUSAO_SOLIDARIA = "A"
    PROTAGONISMO_ATIVO = "B"


class StepType(str, Enum):
    """Tipo de step na trilha."""
    CONTENT = "content"      # Apresentação de conteúdo
    QUESTION = "question"    # Pergunta reflexiva
    VIDEO = "video"          # Apresentação de vídeo
    CHOICE = "choice"        # Escolha de caminho
    PAUSE = "pause"          # Pausa intencional


class FeedbackLevel(str, Enum):
    """Nível de feedback baseado na qualidade da resposta."""
    EXCELLENT = "excellent"   # Resposta elaborada e reflexiva
    GOOD = "good"            # Resposta adequada
    DEVELOPING = "developing" # Resposta superficial, precisa aprofundar
    NEEDS_SUPPORT = "needs_support"  # Resposta vaga ou fora de contexto


# ══════════════════════════════════════════════════════════════
# Estado da Sessão
# ══════════════════════════════════════════════════════════════

class ChatState(BaseModel):
    """Estado da sessão de chat."""
    
    current_step: str = Field(
        default="t01_s1_intro",
        description="ID do step atual"
    )
    completed_steps: list[str] = Field(
        default_factory=list,
        description="Lista de steps já completados"
    )
    caminho_escolhido: Optional[Literal["A", "B"]] = Field(
        default=None,
        description="Caminho escolhido no step de escolha (A ou B)"
    )
    lesson_completed: bool = Field(
        default=False,
        description="Flag indicando se a trilha foi finalizada"
    )
    waiting_for_response: bool = Field(
        default=False,
        description="Flag indicando se está aguardando resposta do docente"
    )
    etapa_docente: Optional[str] = Field(
        default=None,
        description="Etapa de ensino do docente (Anos Iniciais, Educação Infantil, etc)"
    )
    
    # Histórico interno (não exposto ao usuário)
    internal_evaluations: dict[str, FeedbackLevel] = Field(
        default_factory=dict,
        description="Avaliações internas das respostas por step"
    )


# ══════════════════════════════════════════════════════════════
# Configuração de Steps
# ══════════════════════════════════════════════════════════════

class StepConfig(BaseModel):
    """Configuração de um step da trilha."""
    
    id: str = Field(description="ID único do step")
    type: StepType = Field(description="Tipo do step")
    content_file: Optional[str] = Field(
        default=None,
        description="Arquivo de conteúdo associado"
    )
    has_question: bool = Field(
        default=False,
        description="Se o step inclui uma pergunta"
    )
    question: Optional[str] = Field(
        default=None,
        description="Pergunta do step (se houver)"
    )
    next_step: Optional[str] = Field(
        default=None,
        description="Próximo step na sequência"
    )


class RubricCriteria(BaseModel):
    """Critérios de avaliação (rubrica) para uma pergunta."""
    
    question: str = Field(description="A pergunta sendo avaliada")
    excellent: str = Field(description="Critério para resposta excelente")
    good: str = Field(description="Critério para resposta boa")
    developing: str = Field(description="Critério para resposta em desenvolvimento")
    needs_support: str = Field(description="Critério para resposta que precisa de apoio")


# ══════════════════════════════════════════════════════════════
# Outputs dos Subagentes
# ══════════════════════════════════════════════════════════════

class ContentOutput(BaseModel):
    """Output do subagente de apresentação de conteúdo."""
    
    content: str = Field(description="Conteúdo formatado para apresentar")
    has_video: bool = Field(default=False, description="Se inclui vídeo")
    video_url: Optional[str] = Field(default=None, description="URL do vídeo se houver")
    transition_question: Optional[str] = Field(
        default=None,
        description="Pergunta de transição para a próxima etapa"
    )


class QuestionOutput(BaseModel):
    """Output do subagente de perguntas."""
    
    question: str = Field(description="Pergunta a ser feita ao docente")
    context: Optional[str] = Field(
        default=None,
        description="Contexto adicional antes da pergunta"
    )
    is_multiple_part: bool = Field(
        default=False,
        description="Se é parte de uma série de perguntas"
    )
    part_number: Optional[int] = Field(
        default=None,
        description="Número da parte se for série"
    )
    total_parts: Optional[int] = Field(
        default=None,
        description="Total de partes na série"
    )


class FeedbackOutput(BaseModel):
    """Output do subagente de feedback."""
    
    acknowledgment: str = Field(description="Acolhimento inicial")
    strength_analysis: str = Field(description="Análise do ponto forte identificado")
    suggestions: list[str] = Field(description="Sugestões construtivas (1-2)")
    connections: str = Field(description="Conexões formativas com os pilares")
    synthesis: str = Field(description="Síntese final motivadora")
    internal_evaluation: FeedbackLevel = Field(
        description="Avaliação interna (não mostrar ao usuário)"
    )


class OrchestratorOutput(BaseModel):
    """Output do orquestrador para decidir próxima ação."""
    
    action: Literal["present_content", "ask_question", "give_feedback", "advance_step", "end_lesson"] = Field(
        description="Ação a ser tomada"
    )
    reasoning: str = Field(description="Raciocínio para a decisão")
    target_step: Optional[str] = Field(
        default=None,
        description="Step alvo se for avançar"
    )
    detected_path_choice: Optional[Literal["A", "B"]] = Field(
        default=None,
        description="Caminho detectado na resposta do usuário"
    )


# ══════════════════════════════════════════════════════════════
# Request/Response para API
# ══════════════════════════════════════════════════════════════

class ChatRequest(BaseModel):
    """Request para o endpoint de chat."""
    
    message: str = Field(description="Mensagem do docente")
    session_id: Optional[str] = Field(
        default=None,
        description="ID da sessão para manter contexto"
    )


class ChatResponse(BaseModel):
    """Response do endpoint de chat."""
    
    reply: str = Field(description="Resposta do tutor")
    step_id: str = Field(description="ID do step atual")
    next_step_id: Optional[str] = Field(
        default=None,
        description="ID do próximo step"
    )
    state: ChatState = Field(description="Estado atualizado da sessão")
