"""
Instruções específicas para cada step do Trilho 01.
"""

from typing import Optional
from ..constants import TRILHO01_COMPETENCIAS


# Labels amigáveis para cada step
STEP_LABELS: dict[str, str] = {
    "t01_s1_intro": "Introdução",
    "t01_s2_video01": "Vídeo 01",
    "t01_s3_texto_abertura": "Texto de Abertura",
    "t01_s4_pergunta_abertura": "Reflexão Inicial",
    "t01_s5_competencias": "Competências",
    "t01_s6_texto_articulacao": "Articulação",
    "t01_s7_q1": "Pergunta 1/5",
    "t01_s8_q2": "Pergunta 2/5",
    "t01_s9_q3": "Pergunta 3/5",
    "t01_s10_q4": "Pergunta 4/5",
    "t01_s11_q5": "Pergunta 5/5",
    "t01_s12_video02": "Vídeo Situação-Problema",
    "t01_s13_texto_complementar": "Texto Complementar",
    "t01_s14_perguntas_video02": "Reflexão do Vídeo",
    "t01_s15_pausa_intencional": "Pausa Intencional",
    "t01_s16_escolha_caminho": "Escolha de Caminho",
    "t01_s17_video03_escolhido": "Vídeo do Caminho",
    "t01_s18_video03_outro": "Vídeo Alternativo",
    "t01_s19_reflexao_caminhos": "Reflexão Final",
    "t01_s20_conclusao_encerramento": "Conclusão",
}


def get_step_instruction(step_id: str, content: Optional[str] = None, caminho: Optional[str] = None) -> str:
    """
    Retorna a instrução específica para um step.
    
    Args:
        step_id: ID do step
        content: Conteúdo carregado do arquivo .md (se houver)
        caminho: Caminho escolhido pelo docente (A ou B)
    
    Returns:
        Instrução formatada para o step.
    """
    instructions = {
        "t01_s1_intro": _get_intro_instruction(content),
        "t01_s2_video01": _get_video01_instruction(),
        "t01_s3_texto_abertura": _get_texto_abertura_instruction(content),
        "t01_s4_pergunta_abertura": _get_pergunta_abertura_instruction(),
        "t01_s5_competencias": _get_competencias_instruction(),
        "t01_s6_texto_articulacao": _get_texto_articulacao_instruction(content),
        "t01_s7_q1": _get_question_instruction(1, "Como você identifica, em sala, os sinais de dispersão, ansiedade ou falta de foco entre seus estudantes?"),
        "t01_s8_q2": _get_question_instruction(2, "Quais estratégias você utiliza para favorecer atenção e concentração durante suas aulas?"),
        "t01_s9_q3": _get_question_instruction(3, "De que forma você estimula atitudes de empatia e autorregulação emocional entre os estudantes?"),
        "t01_s10_q4": _get_question_instruction(4, "Como você garante que os objetivos das atividades e avaliações estejam alinhados para apoiar a aprendizagem?"),
        "t01_s11_q5": _get_question_instruction(5, "Em que momentos sua prática docente integra valores e princípios que fortalecem vínculos e dão sentido à formação dos estudantes?"),
        "t01_s12_video02": _get_video02_instruction(),
        "t01_s13_texto_complementar": _get_texto_complementar_instruction(content),
        "t01_s14_perguntas_video02": _get_perguntas_video02_instruction(),
        "t01_s15_pausa_intencional": _get_pausa_instruction(),
        "t01_s16_escolha_caminho": _get_escolha_caminho_instruction(),
        "t01_s17_video03_escolhido": _get_video03_instruction(caminho, is_chosen=True),
        "t01_s18_video03_outro": _get_video03_instruction(caminho, is_chosen=False),
        "t01_s19_reflexao_caminhos": _get_reflexao_caminhos_instruction(),
        "t01_s20_conclusao_encerramento": _get_conclusao_instruction(content),
    }
    
    return instructions.get(step_id, f"[Step não encontrado: {step_id}]")


def _get_intro_instruction(content: Optional[str]) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Introdução e Contextualização
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente os ícones integrados e os pilares correspondentes à trilha.
2. Leia o texto de apresentação abaixo em tom acolhedor e conversacional.
3. Após a apresentação, faça a pergunta de engajamento.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}

PERGUNTA DE ENGAJAMENTO (fazer ao final):
👉 "Antes de começarmos, me conte: você leciona para qual etapa? Anos Iniciais ou Educação Infantil? Isso me ajudará a contextualizar melhor nossas reflexões."

Aguarde a resposta do docente antes de prosseguir.
"""


def _get_video01_instruction() -> str:
    return """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo 01 — Abertura
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Mencione que há um vídeo de abertura para assistir.
2. Insira o iframe do vídeo: <iframe src='https://example.com/video01-placeholder' width='560' height='315' frameborder='0' allowfullscreen></iframe>
3. Diga: "Assista ao vídeo de abertura com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_texto_abertura_instruction(content: Optional[str]) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Texto de Abertura
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o texto de abertura da dimensão.
2. Após apresentar o texto, indique que na sequência virá uma pergunta de reflexão.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_pergunta_abertura_instruction() -> str:
    return """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta de Reflexão Inicial
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta de reflexão e aguarde a resposta:

👉 "Na sua prática, quais situações mais desafiadoras você encontra para manter o foco e engajar seus alunos?"

Após a resposta, aplique o fluxo de feedback obrigatório (acolhimento → ponto forte → sugestão → conexões → síntese).

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_competencias_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Competências da Trilha
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Apresente a lista de competências da trilha:

{TRILHO01_COMPETENCIAS}

---

Após apresentar, faça uma breve síntese:
"Neste trilho, sua prática docente será ampliada para contemplar as dimensões Corpo, Mente e Espírito do desenvolvimento humano. Você será convidado a fundamentar suas escolhas pedagógicas em evidências científicas e princípios da neurociência."

Depois, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_texto_articulacao_instruction(content: Optional[str]) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Texto de Articulação
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o texto de articulação.
2. Após apresentar, informe que agora virão 5 perguntas reflexivas, uma de cada vez.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_question_instruction(question_number: int, question: str) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva {question_number} de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "{question}"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_video02_instruction() -> str:
    return """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo 02 — Situação-Problema
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Mencione que há um vídeo de situação-problema para assistir.
2. Contextualize: este vídeo mostra um dilema comum em sala de aula.
3. Insira o iframe: <iframe src='https://example.com/video02-placeholder' width='560' height='315' frameborder='0' allowfullscreen></iframe>
4. Diga: "Assista ao vídeo com atenção, relacionando os dilemas apresentados às suas próprias experiências docentes. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_texto_complementar_instruction(content: Optional[str]) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Texto Complementar
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o texto complementar.
2. Após apresentar, indique que virão perguntas de reflexão sobre o vídeo.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_perguntas_video02_instruction() -> str:
    return """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Perguntas sobre o Vídeo Situação-Problema
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça as seguintes perguntas reflexivas, UMA de cada vez. Após cada resposta, aplique feedback antes de fazer a próxima:

1️⃣ "Você já viveu algo semelhante? Como reagiu diante dessa diversidade de ritmos, emoções e necessidades?"

2️⃣ "Quais estratégias utilizou para tentar manter o foco e o engajamento da turma?"

3️⃣ "De que forma buscou alinhar seu planejamento (objetivos, recursos e avaliação) com as situações que surgiram em sala?"

4️⃣ "Como os valores cristãos (solidariedade, acolhimento, propósito, justiça) apareceram — ou poderiam ter aparecido — em sua postura diante desse desafio?"

IMPORTANTE: Faça UMA pergunta por vez. Aguarde a resposta. Aplique feedback. Só então faça a próxima.

Após responder todas as 4 perguntas e dar feedbacks, indique que virá uma pausa intencional para reflexão e pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_pausa_instruction() -> str:
    return """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pausa Intencional
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Conduza uma pausa guiada de reflexão:

"Após refletir sobre sua experiência docente, faça uma pausa intencional. 

Esse momento é para se colocar no lugar da professora do vídeo diante do desafio de conduzir uma aula em que os estudantes apresentam ritmos diferentes, dispersão e falta de propósito.

Projete como você enfrentaria esse desafio em sua própria sala de aula, de modo a:
• Favorecer o desenvolvimento integral dos estudantes
• Utilizar estratégias sustentadas por evidências
• Manter coerência pedagógica
• Iluminar a prática com os valores cristãos

Respire fundo. Quando estiver pronto(a), me avise para continuarmos."

Após o docente indicar que está pronto, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_escolha_caminho_instruction() -> str:
    return """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Escolha de Caminhos
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Apresente os dois caminhos possíveis e peça que o docente escolha:

"Não existe um caminho único ou perfeito. Cada escolha traz vantagens e limites. O mais importante é refletir sobre as implicações pedagógicas e emocionais de cada decisão.

É hora de se colocar como protagonista. Escolha um dos caminhos:

**🅰️ Caminho Inclusão Solidária:**
'Eu adaptaria a aula para apoiar os estudantes com mais dificuldades, integrando atividades que fortaleçam atenção, autorregulação e empatia.'

**🅱️ Caminho Protagonismo Ativo:**
'Eu avançaria no conteúdo para manter engajados os estudantes que já dominam o conteúdo, criando momentos posteriores de apoio personalizado para os demais.'

👉 Qual caminho você escolhe: A ou B?"

IMPORTANTE: Após o docente responder, registre internamente a escolha (A = Inclusão Solidária, B = Protagonismo Ativo) para os próximos steps.

Após a escolha, faça a pergunta de reflexão:
"Quais seriam os benefícios e os riscos pedagógicos de seguir esse caminho?"

Aplique feedback à reflexão do docente.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_video03_instruction(caminho: Optional[str], is_chosen: bool) -> str:
    if caminho == "A":
        chosen_name = "Inclusão Solidária"
        other_name = "Protagonismo Ativo"
        chosen_video = "inclusao-solidaria"
        other_video = "protagonismo-ativo"
    elif caminho == "B":
        chosen_name = "Protagonismo Ativo"
        other_name = "Inclusão Solidária"
        chosen_video = "protagonismo-ativo"
        other_video = "inclusao-solidaria"
    else:
        return """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo 03
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
O docente ainda não escolheu um caminho. Pergunte qual caminho ele deseja seguir primeiro:
- A (Inclusão Solidária) 
- B (Protagonismo Ativo)
"""

    if is_chosen:
        video_name = chosen_name
        video_id = chosen_video
        intro = f"Você escolheu o caminho {chosen_name}. Vamos assistir ao vídeo correspondente."
    else:
        video_name = other_name
        video_id = other_video
        intro = f"Agora, para ampliar sua perspectiva, convido você a assistir também ao vídeo do caminho {other_name}."

    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo 03 — Caminho {video_name}
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
{intro}

Mencione que há um vídeo para assistir e insira o iframe:
<iframe src='https://example.com/video03-{video_id}-placeholder' width='560' height='315' frameborder='0' allowfullscreen></iframe>

Diga: "Assista ao vídeo com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_reflexao_caminhos_instruction() -> str:
    return """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Reflexão sobre os Caminhos
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Conduza a reflexão final sobre os dois caminhos:

"Você assistiu dois cenários possíveis para lidar com a mesma situação:

• **Inclusão Solidária** → prioriza apoiar os estudantes com mais dificuldades
• **Protagonismo Ativo** → mantém engajados os que já avançaram

Agora reflita:

👉 O que cada caminho favorece em termos de aprendizagem e desenvolvimento integral?

👉 Quais riscos ou limitações cada escolha traz?

👉 De que forma cada opção se conecta aos fundamentos da prática docente: desenvolvimento integral, ensino baseado em evidências, coerência pedagógica e valores cristãos?

👉 Se fosse a sua sala de aula, qual seria o seu próprio caminho? Quais estratégias aplicaria para equilibrar ritmos, engajar estudantes e dar sentido ao aprendizado?"

Faça UMA pergunta por vez. Aplique feedback após cada resposta.

IMPORTANTE: Valorize ambos os caminhos. Não existe resposta certa ou errada. Destaque que o valor está na intencionalidade e reflexão contínua.

Após todas as reflexões e feedbacks, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_conclusao_instruction(content: Optional[str]) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Conclusão e Encerramento
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o texto de conclusão.
2. Faça a pergunta final de encerramento.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}

PERGUNTA FINAL:
👉 "Qual foi sua maior reflexão ou aprendizado nesta trilha sobre promover o desenvolvimento integral do estudante?"

Após a resposta:
1. Aplique o fluxo de feedback completo
2. Parabenize o docente pela conclusão do Trilho 01
3. Informe que a trilha foi finalizada
4. Deixe claro que o docente pode continuar tirando dúvidas sobre qualquer etapa, mesmo após a finalização
5. Use uma mensagem como: "Parabéns por concluir o Trilho 01! A trilha está finalizada, mas você pode continuar tirando dúvidas sobre qualquer etapa sempre que precisar."

Este é o último step. Após o feedback final, a trilha está finalizada, mas o chat permanece ativo para dúvidas.
"""
