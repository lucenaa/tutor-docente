"""
Trilho 01 Steps - Contexto específico de cada step, incluindo gabaritos internos.
"""

import os
from typing import Optional

# Diretório base dos conteúdos
CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "content", "trilho01")


def load_content(filename: str) -> str:
    """Carrega conteúdo de um arquivo .md"""
    filepath = os.path.join(CONTENT_DIR, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Conteúdo não encontrado: {filename}]"


# Configuração de cada step: tipo (content/question), arquivo associado, etc.
STEP_CONFIGS = {
    "t01_s1_intro": {
        "type": "content",
        "content_file": "apresentacao.md",
        "has_question": True,
    },
    "t01_s2_video01": {
        "type": "content",
        "content_file": "video01.md",
        "has_question": False,
    },
    "t01_s3_texto_abertura": {
        "type": "content",
        "content_file": "texto_abertura.md",
        "has_question": False,
    },
    "t01_s4_pergunta_abertura": {
        "type": "question",
        "content_file": None,
        "has_question": True,
    },
    "t01_s5_competencias": {
        "type": "content",
        "content_file": None,  # Competências inline no prompt
        "has_question": False,
    },
    "t01_s6_texto_articulacao": {
        "type": "content",
        "content_file": "texto_articulacao.md",
        "has_question": False,
    },
    "t01_s7_q1": {"type": "question", "content_file": None, "has_question": True},
    "t01_s8_q2": {"type": "question", "content_file": None, "has_question": True},
    "t01_s9_q3": {"type": "question", "content_file": None, "has_question": True},
    "t01_s10_q4": {"type": "question", "content_file": None, "has_question": True},
    "t01_s11_q5": {"type": "question", "content_file": None, "has_question": True},
    "t01_s12_video02": {
        "type": "content",
        "content_file": "video02.md",
        "has_question": False,
    },
    "t01_s13_texto_complementar": {
        "type": "content",
        "content_file": "texto_complementar.md",
        "has_question": False,
    },
    "t01_s14_perguntas_video02": {
        "type": "question",
        "content_file": None,
        "has_question": True,
    },
    "t01_s15_pausa_intencional": {
        "type": "content",
        "content_file": None,
        "has_question": False,
    },
    "t01_s16_escolha_caminho": {
        "type": "question",
        "content_file": None,
        "has_question": True,
    },
    "t01_s17_video03_escolhido": {
        "type": "content",
        "content_file": None,  # Dinâmico baseado no state
        "has_question": False,
    },
    "t01_s18_video03_outro": {
        "type": "content",
        "content_file": None,  # Dinâmico baseado no state
        "has_question": False,
    },
    "t01_s19_reflexao_caminhos": {
        "type": "question",
        "content_file": None,
        "has_question": True,
    },
    "t01_s20_conclusao_encerramento": {
        "type": "content",
        "content_file": "conclusao.md",
        "has_question": True,  # Pergunta final de encerramento
    },
}

# Gabaritos internos (NUNCA revelar ao usuário)
_INTERNAL_RUBRICS = {
    "t01_s7_q1": {
        "pergunta": "Como você identifica, em sala, os sinais de dispersão, ansiedade ou falta de foco entre seus estudantes?",
        "atende": "Reconhece indicadores claros (inquietação, isolamento, perda de atenção) e relaciona à necessidade de adaptação pedagógica e apoio emocional.",
        "parcial": "Identifica sinais superficiais sem aprofundar em causas ou implicações.",
        "nao_atende": "Não apresenta critérios de observação ou minimiza os sinais.",
    },
    "t01_s8_q2": {
        "pergunta": "Quais estratégias você utiliza para favorecer atenção e concentração durante suas aulas?",
        "atende": "Usa práticas baseadas em evidências: rotinas claras, técnicas de atenção plena, gamificação equilibrada, alternância de estímulos.",
        "parcial": "Cita estratégias genéricas ou pouco estruturadas.",
        "nao_atende": "Não apresenta estratégias intencionais ou atribui o foco apenas à responsabilidade do aluno.",
    },
    "t01_s9_q3": {
        "pergunta": "De que forma você estimula atitudes de empatia e autorregulação emocional entre os estudantes?",
        "atende": "Promove rodas de conversa, trabalhos colaborativos, práticas de escuta, momentos de silêncio/reflexão e modelagem de atitudes.",
        "parcial": "Reconhece a importância, mas cita ações pontuais ou pouco sistemáticas.",
        "nao_atende": "Não considera a empatia ou a autorregulação como parte de sua prática docente.",
    },
    "t01_s10_q4": {
        "pergunta": "Como você garante que os objetivos das atividades e avaliações estejam alinhados para apoiar a aprendizagem?",
        "atende": "Demonstra clareza de objetivos vinculados à BNCC, seleciona atividades coerentes e aplica avaliação formativa/responsiva.",
        "parcial": "Apresenta alinhamento parcial, mas sem consistência entre objetivos, atividades e avaliação.",
        "nao_atende": "Trata currículo, atividades e avaliação de forma desconectada ou sem referência a evidências.",
    },
    "t01_s11_q5": {
        "pergunta": "Em que momentos sua prática docente integra valores e princípios que fortalecem vínculos e dão sentido à formação dos estudantes?",
        "atende": "Integra valores cristãos e éticos em situações concretas (dilemas, projetos sociais, celebrações, momentos de espiritualidade).",
        "parcial": "Reconhece valores, mas de forma genérica ou pouco aplicada ao cotidiano.",
        "nao_atende": "Não menciona integração de valores ou reduz a prática apenas a conteúdos acadêmicos.",
    },
    "t01_s14_perguntas_video02": {
        "pergunta": "Você já viveu uma situação semelhante à apresentada no vídeo? Descreva como reagiu e quais estratégias utilizou.",
        "atende": "Relata situação concreta, descreve reações de forma consciente e apresenta estratégias pedagógicas intencionais. Faz conexão com o desenvolvimento integral.",
        "parcial": "Relata experiência de forma vaga, sem detalhar estratégias ou sem clareza de intencionalidade.",
        "nao_atende": "Não descreve situação real ou responde genericamente, sem estratégias ou reflexão.",
    },
}


def get_step_context(step_id: str, state: Optional[dict] = None) -> str:
    """
    Retorna o contexto específico do step para compor o system prompt.
    Inclui instruções, conteúdo a apresentar e pergunta a fazer.
    """
    state = state or {}
    caminho = state.get("caminho_escolhido")
    completed_steps = state.get("completed_steps", [])
    
    # Verificar se o step já foi completado
    step_already_completed = step_id in completed_steps
    
    # Instrução base para evitar repetição
    repetition_warning = ""
    if step_already_completed:
        repetition_warning = """
⚠️ ATENÇÃO: Este step já foi apresentado anteriormente. 
- NÃO apresente o conteúdo novamente.
- Se o docente pedir para continuar, apenas confirme e avance para o próximo step.
- Se o docente fizer uma pergunta ou comentário, responda de forma breve e contextualizada.
"""

    contexts = {
        "t01_s1_intro": f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Introdução e Contextualização
═══════════════════════════════════════════════════════════════
{repetition_warning}
INSTRUÇÃO:
1. {"Se você JÁ apresentou este conteúdo, apenas aguarde confirmação ou responda perguntas do docente." if step_already_completed else "Apresente os ícones integrados e os pilares correspondentes à trilha."}
2. {"NÃO repita o conteúdo." if step_already_completed else "Leia o texto de apresentação abaixo em tom acolhedor e conversacional."}
3. {"Aguarde o docente indicar que está pronto para continuar." if step_already_completed else "Após a apresentação, faça a pergunta de engajamento."}

CONTEÚDO A APRESENTAR:
{load_content("apresentacao.md")}

PERGUNTA DE ENGAJAMENTO (fazer ao final):
👉 "Antes de começarmos, me conte: você leciona para qual etapa? Anos Iniciais ou Educação Infantil? Isso me ajudará a contextualizar melhor nossas reflexões."

Aguarde a resposta do docente antes de prosseguir.
""",
        "t01_s2_video01": f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo 01 — Abertura
═══════════════════════════════════════════════════════════════
{repetition_warning}
INSTRUÇÃO:
1. {"Se você JÁ apresentou este vídeo, apenas aguarde confirmação do docente." if step_already_completed else "Mencione que há um vídeo de abertura para assistir."}
2. {"NÃO repita o conteúdo do vídeo." if step_already_completed else "Insira um iframe embeddado do vídeo usando: <iframe src=\"https://example.com/video01-placeholder\" width=\"560\" height=\"315\" frameborder=\"0\" allowfullscreen></iframe>"}
3. Diga: "Assista ao vídeo de abertura com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s3_texto_abertura": f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Texto de Abertura
═══════════════════════════════════════════════════════════════
{repetition_warning}
INSTRUÇÃO:
1. {"Se você JÁ apresentou este texto, apenas aguarde confirmação. NÃO repita." if step_already_completed else "Apresente o texto de abertura da dimensão."}
2. Após apresentar o texto, indique que na sequência virá uma pergunta de reflexão.

CONTEÚDO A APRESENTAR:
{load_content("texto_abertura.md")}

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s4_pergunta_abertura": """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta de Reflexão Inicial
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta de reflexão e aguarde a resposta:

👉 "Na sua prática, quais situações mais desafiadoras você encontra para manter o foco e engajar seus alunos?"

Após a resposta, aplique o fluxo de feedback obrigatório (acolhimento → ponto forte → sugestão → conexões → síntese).

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s5_competencias": f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Competências da Trilha
═══════════════════════════════════════════════════════════════
{repetition_warning}
INSTRUÇÃO:
{"Se você JÁ apresentou as competências, NÃO as apresente novamente. Apenas aguarde confirmação ou responda perguntas do docente." if step_already_completed else "Apresente a lista de competências da trilha:"}

**Competências da Dimensão 1 — Desenvolvimento Integral**

**1.1** Conceber estratégias que favoreçam o desenvolvimento integral do estudante, contemplando de forma equilibrada os aspectos cognitivo, socioemocional, psicomotor, físico e espiritual, com foco na formação de valores que promovam corpo são, mente sã e espírito pleno.

**1.2** Planejar e avaliar criticamente práticas pedagógicas baseadas em evidências e princípios da neurociência, como atenção, engajamento ativo, feedback (devolutiva ao estudante) e consolidação da aprendizagem.

**1.3** Orquestrar a coerência pedagógica sistêmica, alinhando objetivos, avaliações, recursos e estratégias de ensino.

**1.4** Integrar e incorporar criativamente os valores católicos como fundamento ético e espiritual da prática pedagógica, cultivando liberdade, excelência, transparência e transcendência.

---

Após apresentar, faça uma breve síntese:
"Neste trilho, sua prática docente será ampliada para contemplar as dimensões Corpo, Mente e Espírito do desenvolvimento humano. Você será convidado a fundamentar suas escolhas pedagógicas em evidências científicas e princípios da neurociência."

Depois, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s6_texto_articulacao": f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Texto de Articulação
═══════════════════════════════════════════════════════════════
{repetition_warning}
INSTRUÇÃO:
1. {"Se você JÁ apresentou este texto, apenas aguarde confirmação. NÃO repita." if step_already_completed else "Apresente o texto de articulação."}
2. Após apresentar, informe que agora virão 5 perguntas reflexivas, uma de cada vez.

CONTEÚDO A APRESENTAR:
{load_content("texto_articulacao.md")}

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s7_q1": """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 1 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Como você identifica, em sala, os sinais de dispersão, ansiedade ou falta de foco entre seus estudantes?"

CRITÉRIOS DE AVALIAÇÃO (uso interno — NÃO mencionar):
- Bom: Reconhece indicadores claros (inquietação, isolamento, perda de atenção) e relaciona à necessidade de adaptação pedagógica.
- Desenvolver: Identifica sinais superficiais sem aprofundar.
- Apoiar: Não apresenta critérios de observação.

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s8_q2": """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 2 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Quais estratégias você utiliza para favorecer atenção e concentração durante suas aulas?"

CRITÉRIOS DE AVALIAÇÃO (uso interno — NÃO mencionar):
- Bom: Usa práticas baseadas em evidências (rotinas claras, atenção plena, alternância de estímulos).
- Desenvolver: Cita estratégias genéricas ou pouco estruturadas.
- Apoiar: Não apresenta estratégias intencionais.

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s9_q3": """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 3 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "De que forma você estimula atitudes de empatia e autorregulação emocional entre os estudantes?"

CRITÉRIOS DE AVALIAÇÃO (uso interno — NÃO mencionar):
- Bom: Promove rodas de conversa, trabalhos colaborativos, práticas de escuta e reflexão.
- Desenvolver: Reconhece a importância, mas cita ações pontuais.
- Apoiar: Não considera empatia/autorregulação como parte da prática.

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s10_q4": """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 4 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Como você garante que os objetivos das atividades e avaliações estejam alinhados para apoiar a aprendizagem?"

CRITÉRIOS DE AVALIAÇÃO (uso interno — NÃO mencionar):
- Bom: Demonstra clareza de objetivos vinculados à BNCC, atividades coerentes e avaliação formativa.
- Desenvolver: Apresenta alinhamento parcial, sem consistência.
- Apoiar: Trata currículo, atividades e avaliação de forma desconectada.

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s11_q5": """
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 5 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Em que momentos sua prática docente integra valores e princípios que fortalecem vínculos e dão sentido à formação dos estudantes?"

CRITÉRIOS DE AVALIAÇÃO (uso interno — NÃO mencionar):
- Bom: Integra valores cristãos e éticos em situações concretas.
- Desenvolver: Reconhece valores de forma genérica.
- Apoiar: Não menciona integração de valores.

Aplique o fluxo de feedback após a resposta.

Depois do feedback, informe que agora será apresentado um vídeo com uma situação-problema e pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s12_video02": f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo 02 — Situação-Problema
═══════════════════════════════════════════════════════════════
{repetition_warning}
INSTRUÇÃO:
1. {"Se você JÁ apresentou este vídeo, apenas aguarde confirmação. NÃO repita o conteúdo." if step_already_completed else "Mencione que há um vídeo de situação-problema para assistir."}
2. {"NÃO repita a contextualização." if step_already_completed else "Contextualize: este vídeo mostra um dilema comum em sala de aula."}
3. {"NÃO repita o iframe." if step_already_completed else "Insira um iframe embeddado do vídeo usando: <iframe src=\"https://example.com/video02-placeholder\" width=\"560\" height=\"315\" frameborder=\"0\" allowfullscreen></iframe>"}
4. Diga: "Assista ao vídeo com atenção, relacionando os dilemas apresentados às suas próprias experiências docentes. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s13_texto_complementar": f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Texto Complementar
═══════════════════════════════════════════════════════════════
{repetition_warning}
INSTRUÇÃO:
1. {"Se você JÁ apresentou este texto, apenas aguarde confirmação. NÃO repita." if step_already_completed else "Apresente o texto complementar."}
2. Após apresentar, indique que virão perguntas de reflexão sobre o vídeo.

CONTEÚDO A APRESENTAR:
{load_content("texto_complementar.md")}

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
""",
        "t01_s14_perguntas_video02": """
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
""",
        "t01_s15_pausa_intencional": """
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
""",
        "t01_s16_escolha_caminho": """
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
""",
        "t01_s17_video03_escolhido": _get_video03_context(caminho, is_chosen=True),
        "t01_s18_video03_outro": _get_video03_context(caminho, is_chosen=False),
        "t01_s19_reflexao_caminhos": """
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
""",
        "t01_s20_conclusao_encerramento": f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Conclusão e Encerramento
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o texto de conclusão.
2. Faça a pergunta final de encerramento.

CONTEÚDO A APRESENTAR:
{load_content("conclusao.md")}

PERGUNTA FINAL:
👉 "Qual foi sua maior reflexão ou aprendizado nesta trilha sobre promover o desenvolvimento integral do estudante?"

Após a resposta:
1. Aplique o fluxo de feedback completo
2. Parabenize o docente pela conclusão do Trilho 01
3. Informe que a trilha foi finalizada
4. Deixe claro que o docente pode continuar tirando dúvidas sobre qualquer etapa, mesmo após a finalização
5. Use uma mensagem como: "Parabéns por concluir o Trilho 01! A trilha está finalizada, mas você pode continuar tirando dúvidas sobre qualquer etapa sempre que precisar."

Este é o último step. Após o feedback final, a trilha está finalizada, mas o chat permanece ativo para dúvidas.
""",
    }

    return contexts.get(step_id, f"[Step não encontrado: {step_id}]")


def _get_video03_context(caminho: Optional[str], is_chosen: bool) -> str:
    """Helper para gerar contexto do vídeo 03 baseado no caminho escolhido."""
    if caminho == "A":
        chosen_file = "video03_inclusao_solidaria.md"
        chosen_name = "Inclusão Solidária"
        other_file = "video03_protagonismo_ativo.md"
        other_name = "Protagonismo Ativo"
    elif caminho == "B":
        chosen_file = "video03_protagonismo_ativo.md"
        chosen_name = "Protagonismo Ativo"
        other_file = "video03_inclusao_solidaria.md"
        other_name = "Inclusão Solidária"
    else:
        # Caminho não definido ainda
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
        file_to_load = chosen_file
        video_name = chosen_name
        intro = f"Você escolheu o caminho {chosen_name}. Vamos assistir ao vídeo correspondente."
    else:
        file_to_load = other_file
        video_name = other_name
        intro = f"Agora, para ampliar sua perspectiva, convido você a assistir também ao vídeo do caminho {other_name}."

    content = load_content(file_to_load)

    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo 03 — Caminho {video_name}
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
{intro}

Mencione que há um vídeo para assistir e insira um iframe embeddado usando:
<iframe src="https://example.com/video03-{'inclusao-solidaria' if 'Inclusão' in video_name else 'protagonismo-ativo'}-placeholder" width="560" height="315" frameborder="0" allowfullscreen></iframe>

Diga: "Assista ao vídeo com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""

