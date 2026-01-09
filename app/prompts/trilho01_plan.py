"""
Trilho 01 Plan - Definição do plano, ordem dos steps e helpers.
"""

from typing import Optional

TRILHO_01_PLAN_PROMPT = """
═══════════════════════════════════════════════════════════════
TRILHO 01: Desenvolvimento Integral | Situação-Problema
═══════════════════════════════════════════════════════════════

OBJETIVO
Compreender os fundamentos da proposta Verbum (Corpo são, Mente sã e Espírito pleno), articulando:
• Desenvolvimento integral
• Práticas baseadas em evidências
• Coerência pedagógica
• Valores cristãos

ÍCONES INTEGRADOS
🟡 Eu compreendo! | 🟡 Eu proponho! | 🟡 Eu reflito!

PILARES INTEGRADOS
🌱 Mente sã — autorregulação emocional, atenção plena e clareza mental.
☀️ Espírito pleno — propósito, missão e valores como âncoras.

SEQUÊNCIA OBRIGATÓRIA DO TRILHO
1) Introdução e Contextualização
2) Vídeo de Abertura
3) Texto de Abertura + Pergunta
4) Competências
5) Texto de Articulação + 5 Perguntas Reflexivas
6) Vídeo Situação-Problema
7) Texto Complementar + Perguntas
8) Pausa Intencional
9) Escolha de Caminhos (A ou B)
10) Vídeo do Caminho Escolhido
11) Vídeo do Outro Caminho
12) Reflexão sobre os Caminhos
13) Conclusão e Encerramento

REGRAS DO TRILHO
- Siga rigorosamente a ordem dos steps. NUNCA retorne a steps anteriores.
- NUNCA apresente conteúdo de um step que já foi completado, a menos que seja explicitamente solicitado pelo docente.
- NUNCA mencione materiais, vídeos, textos ou referências que não constem nos arquivos fornecidos.
- Não revele gabaritos ou rótulos de avaliação.
- Apresente conteúdo e faça perguntas conforme definido em cada step.
- Mantenha tom acolhedor e formativo em todas as interações.
- Se o docente perguntar sobre algo que não está no material, acolha e redirecione para o conteúdo da trilha.

MATERIAIS DISPONÍVEIS (use APENAS estes):
- apresentacao.md
- video01.md
- texto_abertura.md
- texto_articulacao.md
- video02.md
- texto_complementar.md
- video03_inclusao_solidaria.md
- video03_protagonismo_ativo.md
- conclusao.md

PROIBIDO mencionar:
- "A Coragem de Educar" ou "Teoria do Iceberg" (NÃO consta na trilha)
- Qualquer material, vídeo ou texto que não esteja na lista acima
"""

# Ordem fixa dos steps do Trilho 01
TRILHO01_STEPS_ORDER = [
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


def get_next_step(current_step_id: str) -> Optional[str]:
    """
    Retorna o próximo step_id na sequência, ou None se for o último.
    """
    try:
        idx = TRILHO01_STEPS_ORDER.index(current_step_id)
        if idx < len(TRILHO01_STEPS_ORDER) - 1:
            return TRILHO01_STEPS_ORDER[idx + 1]
        return None
    except ValueError:
        return None


def get_step_index(step_id: str) -> int:
    """
    Retorna o índice do step na ordem (0-based), ou -1 se não encontrado.
    """
    try:
        return TRILHO01_STEPS_ORDER.index(step_id)
    except ValueError:
        return -1


def is_valid_step(step_id: str) -> bool:
    """
    Verifica se o step_id é válido.
    """
    return step_id in TRILHO01_STEPS_ORDER

