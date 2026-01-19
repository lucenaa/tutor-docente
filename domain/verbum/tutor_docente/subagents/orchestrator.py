"""
Orchestrator Subagent - Decide qual ação tomar baseado no estado atual.
"""

from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field
from typing import Literal, Optional

from core.constants import AIModels


class OrchestratorDecision(BaseModel):
    """Schema de saída do orquestrador."""
    
    action: Literal[
        "present_content",
        "present_video", 
        "ask_question",
        "give_feedback",
        "handle_transition",
        "advance_step",
        "present_choice",
        "present_pause",
        "end_lesson",
        "answer_doubt"
    ] = Field(description="Ação a ser tomada")
    
    reasoning: str = Field(description="Raciocínio para a decisão")
    
    detected_ready_to_advance: bool = Field(
        default=False,
        description="Se o usuário indicou que está pronto para avançar"
    )
    
    detected_path_choice: Optional[Literal["A", "B"]] = Field(
        default=None,
        description="Caminho detectado na resposta do usuário (se aplicável)"
    )
    
    detected_video_watched: bool = Field(
        default=False,
        description="Se o usuário indicou que assistiu o vídeo"
    )
    
    is_question_response: bool = Field(
        default=False,
        description="Se a mensagem é uma resposta a uma pergunta reflexiva"
    )


ORCHESTRATOR_INSTRUCTION = """
Você é o orquestrador do Tutor Docente Verbum. Sua função é analisar o estado atual e a mensagem do usuário para decidir qual ação tomar.

ESTADO ATUAL:
- Step atual: {current_step}
- Tipo do step: {_step_type}
- Step já completado: {_step_already_completed}
- Aguardando resposta: {waiting_for_response}
- Caminho escolhido: {caminho_escolhido}
- Lição completada: {lesson_completed}

REGRAS DE DECISÃO:

1. **Se é a primeira interação do step** (step não completado, sem mensagem anterior):
   - Se tipo é "content": action = "present_content"
   - Se tipo é "video": action = "present_video"
   - Se tipo é "question": action = "ask_question"
   - Se tipo é "choice": action = "present_choice"
   - Se tipo é "pause": action = "present_pause"

2. **Se o usuário está respondendo a uma pergunta**:
   - Detecte se é uma resposta reflexiva (não apenas "sim", "ok", etc.)
   - Se for resposta elaborada: action = "give_feedback", is_question_response = True

3. **Se o usuário indicou que quer avançar** (palavras como "sim", "pode prosseguir", "continuar"):
   - detected_ready_to_advance = True
   - action = "advance_step"

4. **Se o usuário indicou que assistiu o vídeo** ("terminei", "assisti", "vi o vídeo"):
   - detected_video_watched = True
   - action = "handle_transition" (perguntar se pode prosseguir)

5. **Se o usuário está escolhendo um caminho**:
   - Detecte se a mensagem contém "A", "B", "Inclusão Solidária" ou "Protagonismo Ativo"
   - Se detectou: detected_path_choice = "A" ou "B"

6. **Se o usuário tem uma dúvida** (identificável por "?", "dúvida", "não entendi"):
   - action = "answer_doubt"

7. **Se a lição está completada**:
   - action = "end_lesson"

IMPORTANTE:
- Analise o contexto completo antes de decidir
- Priorize a experiência do usuário
- Nunca pule etapas sem confirmação
"""

orchestrator_agent = LlmAgent(
    name="Orchestrator",
    model=AIModels.GEMINI_2_5_FLASH,
    description="Analisa o estado e decide a próxima ação do tutor",
    instruction=ORCHESTRATOR_INSTRUCTION,
    output_schema=OrchestratorDecision,
    output_key="orchestrator_decision",
)
