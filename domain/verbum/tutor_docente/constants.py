"""
Constantes específicas do Tutor Docente.
Define steps, rubricas e configurações do Trilho 01.
"""

from typing import Optional
from .types import StepType, StepConfig, RubricCriteria


# ══════════════════════════════════════════════════════════════
# Ordem dos Steps do Trilho 01
# ══════════════════════════════════════════════════════════════

TRILHO01_STEPS_ORDER: list[str] = [
    "t01_s1_intro",
    "t01_s2_video01",
    "t01_s3_texto_abertura",
    "t01_s4_pergunta_abertura",
    "t01_s5_competencias",
    "t01_s6_texto_articulacao",
    "t01_s7_q1",
    "t01_s8_q2",
    "t01_s9_q3",
    "t01_s10_q4",
    "t01_s11_q5",
    "t01_s12_video02",
    "t01_s13_texto_complementar",
    "t01_s14_perguntas_video02",
    "t01_s15_pausa_intencional",
    "t01_s16_escolha_caminho",
    "t01_s17_video03_escolhido",
    "t01_s18_video03_outro",
    "t01_s19_reflexao_caminhos",
    "t01_s20_conclusao_encerramento",
]


# ══════════════════════════════════════════════════════════════
# Configuração de cada Step
# ══════════════════════════════════════════════════════════════

STEP_CONFIGS: dict[str, StepConfig] = {
    "t01_s1_intro": StepConfig(
        id="t01_s1_intro",
        type=StepType.CONTENT,
        content_file="apresentacao.md",
        has_question=True,
        question="Antes de começarmos, me conte: você leciona para qual etapa? Anos Iniciais ou Educação Infantil? Isso me ajudará a contextualizar melhor nossas reflexões."
    ),
    "t01_s2_video01": StepConfig(
        id="t01_s2_video01",
        type=StepType.VIDEO,
        content_file="video01.md",
        has_question=False
    ),
    "t01_s3_texto_abertura": StepConfig(
        id="t01_s3_texto_abertura",
        type=StepType.CONTENT,
        content_file="texto_abertura.md",
        has_question=False
    ),
    "t01_s4_pergunta_abertura": StepConfig(
        id="t01_s4_pergunta_abertura",
        type=StepType.QUESTION,
        has_question=True,
        question="Na sua prática, quais situações mais desafiadoras você encontra para manter o foco e engajar seus alunos?"
    ),
    "t01_s5_competencias": StepConfig(
        id="t01_s5_competencias",
        type=StepType.CONTENT,
        has_question=False
    ),
    "t01_s6_texto_articulacao": StepConfig(
        id="t01_s6_texto_articulacao",
        type=StepType.CONTENT,
        content_file="texto_articulacao.md",
        has_question=False
    ),
    "t01_s7_q1": StepConfig(
        id="t01_s7_q1",
        type=StepType.QUESTION,
        has_question=True,
        question="Como você identifica, em sala, os sinais de dispersão, ansiedade ou falta de foco entre seus estudantes?"
    ),
    "t01_s8_q2": StepConfig(
        id="t01_s8_q2",
        type=StepType.QUESTION,
        has_question=True,
        question="Quais estratégias você utiliza para favorecer atenção e concentração durante suas aulas?"
    ),
    "t01_s9_q3": StepConfig(
        id="t01_s9_q3",
        type=StepType.QUESTION,
        has_question=True,
        question="De que forma você estimula atitudes de empatia e autorregulação emocional entre os estudantes?"
    ),
    "t01_s10_q4": StepConfig(
        id="t01_s10_q4",
        type=StepType.QUESTION,
        has_question=True,
        question="Como você garante que os objetivos das atividades e avaliações estejam alinhados para apoiar a aprendizagem?"
    ),
    "t01_s11_q5": StepConfig(
        id="t01_s11_q5",
        type=StepType.QUESTION,
        has_question=True,
        question="Em que momentos sua prática docente integra valores e princípios que fortalecem vínculos e dão sentido à formação dos estudantes?"
    ),
    "t01_s12_video02": StepConfig(
        id="t01_s12_video02",
        type=StepType.VIDEO,
        content_file="video02.md",
        has_question=False
    ),
    "t01_s13_texto_complementar": StepConfig(
        id="t01_s13_texto_complementar",
        type=StepType.CONTENT,
        content_file="texto_complementar.md",
        has_question=False
    ),
    "t01_s14_perguntas_video02": StepConfig(
        id="t01_s14_perguntas_video02",
        type=StepType.QUESTION,
        has_question=True
    ),
    "t01_s15_pausa_intencional": StepConfig(
        id="t01_s15_pausa_intencional",
        type=StepType.PAUSE,
        has_question=False
    ),
    "t01_s16_escolha_caminho": StepConfig(
        id="t01_s16_escolha_caminho",
        type=StepType.CHOICE,
        has_question=True
    ),
    "t01_s17_video03_escolhido": StepConfig(
        id="t01_s17_video03_escolhido",
        type=StepType.VIDEO,
        has_question=False
    ),
    "t01_s18_video03_outro": StepConfig(
        id="t01_s18_video03_outro",
        type=StepType.VIDEO,
        has_question=False
    ),
    "t01_s19_reflexao_caminhos": StepConfig(
        id="t01_s19_reflexao_caminhos",
        type=StepType.QUESTION,
        has_question=True
    ),
    "t01_s20_conclusao_encerramento": StepConfig(
        id="t01_s20_conclusao_encerramento",
        type=StepType.CONTENT,
        content_file="conclusao.md",
        has_question=True,
        question="Qual foi sua maior reflexão ou aprendizado nesta trilha sobre promover o desenvolvimento integral do estudante?"
    ),
}


# ══════════════════════════════════════════════════════════════
# Rubricas de Avaliação (uso interno - NUNCA revelar ao usuário)
# ══════════════════════════════════════════════════════════════

INTERNAL_RUBRICS: dict[str, RubricCriteria] = {
    "t01_s7_q1": RubricCriteria(
        question="Como você identifica, em sala, os sinais de dispersão, ansiedade ou falta de foco entre seus estudantes?",
        excellent="Reconhece indicadores claros (inquietação, isolamento, perda de atenção) e relaciona à necessidade de adaptação pedagógica e apoio emocional, citando exemplos concretos.",
        good="Reconhece indicadores claros e relaciona à necessidade de adaptação pedagógica.",
        developing="Identifica sinais superficiais sem aprofundar em causas ou implicações.",
        needs_support="Não apresenta critérios de observação ou minimiza os sinais."
    ),
    "t01_s8_q2": RubricCriteria(
        question="Quais estratégias você utiliza para favorecer atenção e concentração durante suas aulas?",
        excellent="Usa práticas baseadas em evidências: rotinas claras, técnicas de atenção plena, gamificação equilibrada, alternância de estímulos, com exemplos de aplicação.",
        good="Usa práticas baseadas em evidências: rotinas claras, técnicas de atenção plena, alternância de estímulos.",
        developing="Cita estratégias genéricas ou pouco estruturadas.",
        needs_support="Não apresenta estratégias intencionais ou atribui o foco apenas à responsabilidade do aluno."
    ),
    "t01_s9_q3": RubricCriteria(
        question="De que forma você estimula atitudes de empatia e autorregulação emocional entre os estudantes?",
        excellent="Promove rodas de conversa, trabalhos colaborativos, práticas de escuta, momentos de silêncio/reflexão e modelagem de atitudes, descrevendo situações concretas.",
        good="Promove rodas de conversa, trabalhos colaborativos, práticas de escuta e momentos de reflexão.",
        developing="Reconhece a importância, mas cita ações pontuais ou pouco sistemáticas.",
        needs_support="Não considera a empatia ou a autorregulação como parte de sua prática docente."
    ),
    "t01_s10_q4": RubricCriteria(
        question="Como você garante que os objetivos das atividades e avaliações estejam alinhados para apoiar a aprendizagem?",
        excellent="Demonstra clareza de objetivos vinculados à BNCC, seleciona atividades coerentes e aplica avaliação formativa/responsiva, com exemplos de alinhamento.",
        good="Demonstra clareza de objetivos vinculados à BNCC, seleciona atividades coerentes e aplica avaliação formativa.",
        developing="Apresenta alinhamento parcial, mas sem consistência entre objetivos, atividades e avaliação.",
        needs_support="Trata currículo, atividades e avaliação de forma desconectada ou sem referência a evidências."
    ),
    "t01_s11_q5": RubricCriteria(
        question="Em que momentos sua prática docente integra valores e princípios que fortalecem vínculos e dão sentido à formação dos estudantes?",
        excellent="Integra valores cristãos e éticos em situações concretas (dilemas, projetos sociais, celebrações, momentos de espiritualidade), descrevendo como isso impacta os estudantes.",
        good="Integra valores cristãos e éticos em situações concretas (dilemas, projetos sociais, momentos de espiritualidade).",
        developing="Reconhece valores, mas de forma genérica ou pouco aplicada ao cotidiano.",
        needs_support="Não menciona integração de valores ou reduz a prática apenas a conteúdos acadêmicos."
    ),
    "t01_s14_perguntas_video02": RubricCriteria(
        question="Você já viveu uma situação semelhante à apresentada no vídeo? Descreva como reagiu e quais estratégias utilizou.",
        excellent="Relata situação concreta, descreve reações de forma consciente e apresenta estratégias pedagógicas intencionais. Faz conexão com o desenvolvimento integral.",
        good="Relata situação concreta, descreve reações e apresenta estratégias pedagógicas intencionais.",
        developing="Relata experiência de forma vaga, sem detalhar estratégias ou sem clareza de intencionalidade.",
        needs_support="Não descreve situação real ou responde genericamente, sem estratégias ou reflexão."
    ),
}


# ══════════════════════════════════════════════════════════════
# Materiais Disponíveis (para validação)
# ══════════════════════════════════════════════════════════════

AVAILABLE_MATERIALS: list[str] = [
    "apresentacao.md",
    "video01.md",
    "texto_abertura.md",
    "texto_articulacao.md",
    "video02.md",
    "texto_complementar.md",
    "video03_inclusao_solidaria.md",
    "video03_protagonismo_ativo.md",
    "conclusao.md",
]


# ══════════════════════════════════════════════════════════════
# Steps que são apenas conteúdo (sem pergunta elaborada)
# ══════════════════════════════════════════════════════════════

CONTENT_ONLY_STEPS: list[str] = [
    "t01_s2_video01",
    "t01_s3_texto_abertura",
    "t01_s5_competencias",
    "t01_s6_texto_articulacao",
    "t01_s12_video02",
    "t01_s13_texto_complementar",
    "t01_s15_pausa_intencional",
    "t01_s17_video03_escolhido",
    "t01_s18_video03_outro",
]


# ══════════════════════════════════════════════════════════════
# Competências do Trilho 01
# ══════════════════════════════════════════════════════════════

TRILHO01_COMPETENCIAS = """
**Competências da Dimensão 1 — Desenvolvimento Integral**

**1.1** Conceber estratégias que favoreçam o desenvolvimento integral do estudante, contemplando de forma equilibrada os aspectos cognitivo, socioemocional, psicomotor, físico e espiritual, com foco na formação de valores que promovam corpo são, mente sã e espírito pleno.

**1.2** Planejar e avaliar criticamente práticas pedagógicas baseadas em evidências e princípios da neurociência, como atenção, engajamento ativo, feedback (devolutiva ao estudante) e consolidação da aprendizagem.

**1.3** Orquestrar a coerência pedagógica sistêmica, alinhando objetivos, avaliações, recursos e estratégias de ensino.

**1.4** Integrar e incorporar criativamente os valores católicos como fundamento ético e espiritual da prática pedagógica, cultivando liberdade, excelência, transparência e transcendência.
"""


# ══════════════════════════════════════════════════════════════
# Helpers
# ══════════════════════════════════════════════════════════════

def get_next_step(current_step_id: str) -> Optional[str]:
    """Retorna o próximo step na sequência, ou None se for o último."""
    try:
        idx = TRILHO01_STEPS_ORDER.index(current_step_id)
        if idx < len(TRILHO01_STEPS_ORDER) - 1:
            return TRILHO01_STEPS_ORDER[idx + 1]
        return None
    except ValueError:
        return None


def get_step_index(step_id: str) -> int:
    """Retorna o índice do step na ordem (0-based), ou -1 se não encontrado."""
    try:
        return TRILHO01_STEPS_ORDER.index(step_id)
    except ValueError:
        return -1


def is_valid_step(step_id: str) -> bool:
    """Verifica se o step_id é válido."""
    return step_id in TRILHO01_STEPS_ORDER


def get_step_config(step_id: str) -> Optional[StepConfig]:
    """Retorna a configuração de um step."""
    return STEP_CONFIGS.get(step_id)


def get_rubric(step_id: str) -> Optional[RubricCriteria]:
    """Retorna a rubrica de um step, se houver."""
    return INTERNAL_RUBRICS.get(step_id)
