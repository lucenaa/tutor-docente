"""
Instruções específicas para cada step do Trilho 01.
Gerado automaticamente pelo script generate_trilho.py
"""

from typing import Optional


# Labels amigáveis para cada step
TRILHO01_STEP_LABELS: dict[str, str] = {
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
    "t01_s20_conclusao_encerramento": "Conclusão"
}


def get_trilho01_step_instruction(step_id: str, content: Optional[str] = None, caminho: Optional[str] = None) -> str:
    """
    Retorna a instrução específica para um step do Trilho 01.
    
    Args:
        step_id: ID do step
        content: Conteúdo carregado do arquivo .md (se houver)
        caminho: Caminho escolhido pelo docente (A ou B)
    
    Returns:
        Instrução formatada para o step.
    """
    instructions = {
        "t01_s1_intro": _get_s1_intro_instruction(content),
        "t01_s2_video01": _get_s2_video01_instruction(),
        "t01_s3_texto_abertura": _get_s3_texto_abertura_instruction(content),
        "t01_s4_pergunta_abertura": _get_s4_pergunta_abertura_instruction(),
        "t01_s5_competencias": _get_s5_competencias_instruction(),
        "t01_s6_texto_articulacao": _get_s6_texto_articulacao_instruction(content),
        "t01_s7_q1": _get_s7_q1_instruction(),
        "t01_s8_q2": _get_s8_q2_instruction(),
        "t01_s9_q3": _get_s9_q3_instruction(),
        "t01_s10_q4": _get_s10_q4_instruction(),
        "t01_s11_q5": _get_s11_q5_instruction(),
        "t01_s12_video02": _get_s12_video02_instruction(),
        "t01_s13_texto_complementar": _get_s13_texto_complementar_instruction(content),
        "t01_s14_perguntas_video02": _get_s14_perguntas_video02_instruction(),
        "t01_s15_pausa_intencional": _get_s15_pausa_intencional_instruction(),
        "t01_s16_escolha_caminho": _get_s16_escolha_caminho_instruction(caminho),
        "t01_s17_video03_escolhido": _get_s17_video03_escolhido_instruction(caminho),
        "t01_s18_video03_outro": _get_s18_video03_outro_instruction(caminho),
        "t01_s19_reflexao_caminhos": _get_s19_reflexao_caminhos_instruction(),
        "t01_s20_conclusao_encerramento": _get_s20_conclusao_encerramento_instruction(content)
    }
    
    return instructions.get(step_id, f"[Step não encontrado: {step_id}]")


def _get_s1_intro_instruction(content: Optional[str] = None) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Introdução
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o conteúdo em tom acolhedor e conversacional.
2. Após apresentar, verifique se há dúvidas.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}


PERGUNTA DE ENGAJAMENTO (fazer ao final):
👉 "Antes de começarmos, me conte: você leciona para qual etapa? Anos Iniciais ou Educação Infantil? Isso me ajudará a contextualizar melhor nossas reflexões."

Aguarde a resposta do docente antes de prosseguir.

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s2_video01_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo 01
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Mencione que há um vídeo para assistir.
2. Insira o iframe do vídeo: <iframe src='https://example.com/video01-placeholder' width='560' height='315' frameborder='0' allowfullscreen></iframe>
3. Diga: "Assista ao vídeo com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s3_texto_abertura_instruction(content: Optional[str] = None) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Texto de Abertura
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o conteúdo em tom acolhedor e conversacional.
2. Após apresentar, verifique se há dúvidas.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}


Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s4_pergunta_abertura_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Reflexão Inicial
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Na sua prática, quais situações mais desafiadoras você encontra para manter o foco e engajar seus alunos?"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s5_competencias_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Competências
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o conteúdo em tom acolhedor e conversacional.
2. Após apresentar, verifique se há dúvidas.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}


Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s6_texto_articulacao_instruction(content: Optional[str] = None) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Articulação
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o conteúdo em tom acolhedor e conversacional.
2. Após apresentar, verifique se há dúvidas.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}


Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s7_q1_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 1 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Como você identifica, em sala, os sinais de dispersão, ansiedade ou falta de foco entre seus estudantes?"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s8_q2_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 2 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Quais estratégias você utiliza para favorecer atenção e concentração durante suas aulas?"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s9_q3_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 3 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "De que forma você estimula atitudes de empatia e autorregulação emocional entre os estudantes?"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s10_q4_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 4 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Como você garante que os objetivos das atividades e avaliações estejam alinhados para apoiar a aprendizagem?"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s11_q5_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pergunta Reflexiva 5 de 5
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Em que momentos sua prática docente integra valores e princípios que fortalecem vínculos e dão sentido à formação dos estudantes?"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s12_video02_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo Situação-Problema
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Mencione que há um vídeo para assistir.
2. Insira o iframe do vídeo: <iframe src='https://example.com/video02-placeholder' width='560' height='315' frameborder='0' allowfullscreen></iframe>
3. Diga: "Assista ao vídeo com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s13_texto_complementar_instruction(content: Optional[str] = None) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Texto Complementar
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o conteúdo em tom acolhedor e conversacional.
2. Após apresentar, verifique se há dúvidas.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}


Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s14_perguntas_video02_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Reflexão do Vídeo
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "[Pergunta não definida]"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s15_pausa_intencional_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Pausa Intencional
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Conduza uma pausa guiada de reflexão:

"Faça uma pausa intencional. Esse momento é para você se colocar no lugar 
do docente diante do desafio apresentado.

Projete como você enfrentaria esse desafio em sua própria sala de aula.

Respire fundo. Quando estiver pronto(a), me avise para continuarmos."

Após o docente indicar que está pronto, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s16_escolha_caminho_instruction(caminho: Optional[str] = None) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Escolha de Caminho
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Apresente os caminhos possíveis e peça que o docente escolha:

"Não existe um caminho único ou perfeito. Cada escolha traz vantagens e limites.

É hora de se colocar como protagonista. Escolha um dos caminhos:

**🅰️ Caminho Inclusão Solidária:**
'Eu adaptaria a aula para apoiar os estudantes com mais dificuldades, integrando atividades que fortaleçam atenção, autorregulação e empatia.'

**🅱️ Caminho Protagonismo Ativo:**
'Eu avançaria no conteúdo para manter engajados os estudantes que já dominam o conteúdo, criando momentos posteriores de apoio personalizado para os demais.'

👉 Qual caminho você escolhe?"

IMPORTANTE: Registre a escolha para os próximos steps.

Após a escolha, faça uma pergunta de reflexão sobre os benefícios e riscos da escolha.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s17_video03_escolhido_instruction(caminho: Optional[str] = None) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo do Caminho
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Mencione que há um vídeo para assistir.
2. Insira o iframe do vídeo: <iframe src='https://example.com/video-placeholder' width='560' height='315' frameborder='0' allowfullscreen></iframe>
3. Diga: "Assista ao vídeo com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s18_video03_outro_instruction(caminho: Optional[str] = None) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Vídeo Alternativo
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Mencione que há um vídeo para assistir.
2. Insira o iframe do vídeo: <iframe src='https://example.com/video-placeholder' width='560' height='315' frameborder='0' allowfullscreen></iframe>
3. Diga: "Assista ao vídeo com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s19_reflexao_caminhos_instruction() -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Reflexão Final
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "[Pergunta não definida]"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""


def _get_s20_conclusao_encerramento_instruction(content: Optional[str] = None) -> str:
    return f"""
═══════════════════════════════════════════════════════════════
STEP ATUAL: Conclusão
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o conteúdo em tom acolhedor e conversacional.
2. Após apresentar, verifique se há dúvidas.

CONTEÚDO A APRESENTAR:
{content or "[Conteúdo não carregado]"}


PERGUNTA DE ENGAJAMENTO (fazer ao final):
👉 "Qual foi sua maior reflexão ou aprendizado nesta trilha sobre promover o desenvolvimento integral do estudante?"

Aguarde a resposta do docente antes de prosseguir.

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
"""

