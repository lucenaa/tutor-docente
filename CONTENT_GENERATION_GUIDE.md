# Guia de Geração de Conteúdo para Trilhas Verbum

> **Objetivo**: Este documento orienta como transformar materiais educacionais originais da Verbum em trilhas estruturadas para o Tutor Docente, definindo steps, arquivos de conteúdo e configurações necessárias.

---

## Índice

1. [Visão Geral](#1-visão-geral)
2. [Estrutura de uma Trilha](#2-estrutura-de-uma-trilha)
3. [Tipos de Steps](#3-tipos-de-steps)
4. [Mapeamento: Material Original → Steps](#4-mapeamento-material-original--steps)
5. [Regras de Quebra de Conteúdo](#5-regras-de-quebra-de-conteúdo)
6. [Formato dos Arquivos de Conteúdo](#6-formato-dos-arquivos-de-conteúdo)
7. [Configuração de Steps (Python)](#7-configuração-de-steps-python)
8. [Checklist de Criação](#8-checklist-de-criação)
9. [Exemplo Completo: Trilho 01](#9-exemplo-completo-trilho-01)
10. [Usando o Script de Geração](#10-usando-o-script-de-geração)

---

## 1. Visão Geral

### O que é uma Trilha?

Uma **trilha** é uma sequência estruturada de **steps** (etapas) que conduzem o docente através de uma formação pedagógica. Cada trilha possui:

- **Tema central**: O assunto principal da formação
- **Objetivo pedagógico**: O que o docente deve aprender/refletir
- **Sequência de steps**: Etapas ordenadas de conteúdo, vídeos, perguntas e reflexões
- **Materiais de apoio**: Arquivos `.md` com textos e roteiros

### Fluxo Geral de uma Trilha

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ INTRODUÇÃO   │──▶│   VÍDEOS     │──▶│   TEXTOS     │
│ Boas-vindas  │   │  de Abertura │   │  Teóricos    │
└──────────────┘   └──────────────┘   └──────────────┘
                                              │
                                              ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  REFLEXÕES   │◀──│  PERGUNTAS   │◀──│ COMPETÊNCIAS │
│   Finais     │   │  Reflexivas  │   │  da Trilha   │
└──────────────┘   └──────────────┘   └──────────────┘
        │
        ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   SITUAÇÃO   │──▶│   ESCOLHA    │──▶│   VÍDEOS     │
│  PROBLEMA    │   │  DE CAMINHO  │   │ ALTERNATIVOS │
└──────────────┘   └──────────────┘   └──────────────┘
                                              │
                                              ▼
                                       ┌──────────────┐
                                       │  CONCLUSÃO   │
                                       │ Encerramento │
                                       └──────────────┘
```

---

## 2. Estrutura de uma Trilha

### 2.1 Quantidade de Steps Recomendada

| Tipo de Trilha | Quantidade de Steps | Duração Estimada |
|----------------|---------------------|------------------|
| Trilha Curta   | 10-15 steps         | 30-45 minutos    |
| Trilha Média   | 15-25 steps         | 45-90 minutos    |
| Trilha Longa   | 25-35 steps         | 90-120 minutos   |

**Recomendação**: Trilhas médias (15-25 steps) são ideais para manter o engajamento.

### 2.2 Estrutura de Diretórios

```
domain/verbum/tutor_docente/
├── content/
│   └── trilhoXX/                    # Conteúdos da trilha
│       ├── apresentacao.md          # Introdução
│       ├── texto_abertura.md        # Texto de abertura
│       ├── texto_articulacao.md     # Texto de articulação
│       ├── texto_complementar.md    # Textos complementares
│       ├── conclusao.md             # Conclusão
│       ├── video01.md               # Roteiro vídeo 1
│       ├── video02.md               # Roteiro vídeo 2
│       └── video03_*.md             # Roteiros vídeos alternativos
├── prompts/
│   ├── trilhoXX_plan.py             # Plano geral da trilha
│   └── step_instructions.py         # Instruções por step (atualizar)
├── constants.py                     # Configurações dos steps (atualizar)
└── types.py                         # Tipos (não alterar)
```

### 2.3 Convenção de Nomenclatura

**Step IDs**: `tXX_sN_descricao`
- `tXX`: Número do trilho (ex: `t01`, `t02`)
- `sN`: Número sequencial do step (ex: `s1`, `s2`, ..., `s20`)
- `descricao`: Descrição curta em snake_case (ex: `intro`, `video01`, `pergunta_abertura`)

**Exemplos**:
- `t01_s1_intro` - Trilho 01, Step 1, Introdução
- `t02_s7_q1` - Trilho 02, Step 7, Pergunta 1
- `t03_s15_escolha_caminho` - Trilho 03, Step 15, Escolha de Caminho

---

## 3. Tipos de Steps

Existem **5 tipos** de steps, cada um com comportamento específico:

### 3.1 CONTENT (Conteúdo)

**Propósito**: Apresentar textos, conceitos ou informações teóricas.

| Atributo | Descrição |
|----------|-----------|
| `type` | `StepType.CONTENT` |
| `content_file` | Nome do arquivo `.md` a carregar |
| `has_question` | `True` se tiver pergunta ao final |
| `question` | Pergunta de engajamento (opcional) |

**Quando usar**:
- Introdução e boas-vindas
- Textos teóricos e conceituais
- Apresentação de competências
- Conclusão e encerramento

**Exemplo de instrução**:
```
STEP ATUAL: Texto de Abertura

INSTRUÇÃO:
1. Apresente o texto de abertura da dimensão.
2. Após apresentar o texto, indique que na sequência virá uma pergunta de reflexão.

CONTEÚDO A APRESENTAR:
{conteúdo do arquivo .md}

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
```

---

### 3.2 VIDEO (Vídeo)

**Propósito**: Apresentar um vídeo para o docente assistir.

| Atributo | Descrição |
|----------|-----------|
| `type` | `StepType.VIDEO` |
| `content_file` | Arquivo `.md` com roteiro (NÃO exibir ao usuário) |
| `has_question` | Geralmente `False` |

**Quando usar**:
- Vídeos de abertura/introdução
- Situações-problema dramatizadas
- Vídeos de caminhos alternativos
- Tutoriais ou demonstrações

**Regras importantes**:
- **NUNCA** mostrar o roteiro do vídeo ao docente
- Inserir iframe com URL do vídeo
- Aguardar confirmação de que assistiu

**Exemplo de instrução**:
```
STEP ATUAL: Vídeo 01 — Abertura

INSTRUÇÃO:
1. Mencione que há um vídeo de abertura para assistir.
2. Insira o iframe: <iframe src='URL_DO_VIDEO' width='560' height='315' frameborder='0' allowfullscreen></iframe>
3. Diga: "Assista ao vídeo com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo.
```

---

### 3.3 QUESTION (Pergunta)

**Propósito**: Fazer perguntas reflexivas e fornecer feedback formativo.

| Atributo | Descrição |
|----------|-----------|
| `type` | `StepType.QUESTION` |
| `has_question` | `True` |
| `question` | A pergunta a ser feita |

**Quando usar**:
- Perguntas reflexivas sobre a prática docente
- Perguntas após vídeos ou textos
- Séries de perguntas (5 perguntas do bloco reflexivo)

**Regras importantes**:
- Fazer **UMA** pergunta por vez
- Aplicar fluxo de feedback após a resposta
- Feedback proporcional à qualidade da resposta

**Exemplo de instrução**:
```
STEP ATUAL: Pergunta Reflexiva 1 de 5

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "Como você identifica, em sala, os sinais de dispersão, ansiedade ou falta de foco entre seus estudantes?"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
```

---

### 3.4 CHOICE (Escolha)

**Propósito**: Apresentar opções e registrar a escolha do docente.

| Atributo | Descrição |
|----------|-----------|
| `type` | `StepType.CHOICE` |
| `has_question` | `True` |

**Quando usar**:
- Escolha entre caminhos pedagógicos
- Decisões sobre abordagens
- Bifurcações na trilha

**Regras importantes**:
- Apresentar claramente as opções (geralmente A e B)
- Registrar a escolha no estado da sessão
- Usar a escolha para determinar vídeos/conteúdos subsequentes

**Exemplo de instrução**:
```
STEP ATUAL: Escolha de Caminhos

INSTRUÇÃO:
Apresente os dois caminhos possíveis:

**🅰️ Caminho Inclusão Solidária:**
'Eu adaptaria a aula para apoiar os estudantes com mais dificuldades...'

**🅱️ Caminho Protagonismo Ativo:**
'Eu avançaria no conteúdo para manter engajados os que já dominam...'

👉 Qual caminho você escolhe: A ou B?

IMPORTANTE: Registre a escolha para os próximos steps.
```

---

### 3.5 PAUSE (Pausa)

**Propósito**: Criar momentos de reflexão intencional.

| Atributo | Descrição |
|----------|-----------|
| `type` | `StepType.PAUSE` |
| `has_question` | `False` |

**Quando usar**:
- Antes de escolhas importantes
- Após vídeos de situação-problema
- Momentos de introspecção

**Exemplo de instrução**:
```
STEP ATUAL: Pausa Intencional

INSTRUÇÃO:
Conduza uma pausa guiada de reflexão:

"Faça uma pausa intencional. Esse momento é para você se colocar no lugar 
da professora do vídeo diante do desafio apresentado.

Respire fundo. Quando estiver pronto(a), me avise para continuarmos."
```

---

## 4. Mapeamento: Material Original → Steps

### 4.1 Tabela de Mapeamento

| Seção do Material Original | Tipo de Step | Arquivo a Criar | Observações |
|---------------------------|--------------|-----------------|-------------|
| Introdução / Boas-vindas | CONTENT | `apresentacao.md` | Inclui ícones e pilares |
| Vídeo de abertura | VIDEO | `video01.md` | Roteiro para contexto interno |
| Texto de abertura da dimensão | CONTENT | `texto_abertura.md` | Contextualiza o tema |
| Pergunta de reflexão inicial | QUESTION | - | Pergunta inline no step |
| Lista de competências | CONTENT | - | Competências da trilha |
| Texto de articulação | CONTENT | `texto_articulacao.md` | Conecta teoria e prática |
| Bloco de perguntas reflexivas | QUESTION (x5) | - | Uma pergunta por step |
| Vídeo de situação-problema | VIDEO | `video02.md` | Dramatização de dilema |
| Texto complementar | CONTENT | `texto_complementar.md` | Aprofundamento |
| Perguntas sobre o vídeo | QUESTION | - | Série de 4 perguntas |
| Pausa para reflexão | PAUSE | - | Momento intencional |
| Escolha de caminhos | CHOICE | - | Bifurcação A/B |
| Vídeo caminho A | VIDEO | `video03_opcao_a.md` | Roteiro do caminho A |
| Vídeo caminho B | VIDEO | `video03_opcao_b.md` | Roteiro do caminho B |
| Reflexão sobre caminhos | QUESTION | - | Comparação dos caminhos |
| Conclusão | CONTENT | `conclusao.md` | Síntese e encerramento |

### 4.2 Exemplo de Transformação

**Material Original** (trecho):
```
## Introdução
Olá, professor! Bem-vindo à Trilha sobre Desenvolvimento Integral...

## Objetivo
Compreender os fundamentos da proposta Verbum...

## Vídeo de Abertura
[Link do vídeo]

## Texto Base
Todo docente certamente já vivenciou momentos desafiadores...

## Perguntas para Reflexão
1. Como você identifica sinais de dispersão?
2. Quais estratégias você utiliza?
3. De que forma você estimula empatia?
...
```

**Transformação em Steps**:

| # | Step ID | Tipo | Conteúdo |
|---|---------|------|----------|
| 1 | `t01_s1_intro` | CONTENT | Introdução + Objetivo → `apresentacao.md` |
| 2 | `t01_s2_video01` | VIDEO | Vídeo de Abertura → `video01.md` |
| 3 | `t01_s3_texto_abertura` | CONTENT | Texto Base → `texto_abertura.md` |
| 4 | `t01_s4_pergunta_abertura` | QUESTION | Pergunta de engajamento |
| 5 | `t01_s5_competencias` | CONTENT | Competências (inline) |
| 6 | `t01_s6_texto_articulacao` | CONTENT | Articulação → `texto_articulacao.md` |
| 7-11 | `t01_s7_q1` ... `t01_s11_q5` | QUESTION | 5 perguntas reflexivas |
| ... | ... | ... | ... |

---

## 5. Regras de Quebra de Conteúdo

### 5.1 Textos

| Regra | Descrição |
|-------|-----------|
| **Tamanho ideal** | 200-500 palavras por arquivo `.md` |
| **Textos longos** | Dividir em múltiplos arquivos (`texto_parte1.md`, `texto_parte2.md`) |
| **Parágrafos** | Manter parágrafos coesos, não quebrar no meio |
| **Seções lógicas** | Respeitar divisões naturais do conteúdo |

### 5.2 Perguntas

| Regra | Descrição |
|-------|-----------|
| **Uma por step** | Cada pergunta reflexiva = 1 step separado |
| **Sequência numerada** | Identificar como "Pergunta 1 de 5", "Pergunta 2 de 5", etc. |
| **Feedback obrigatório** | Toda pergunta requer feedback formativo |
| **Rubricas** | Criar rubrica interna para calibrar feedback |

### 5.3 Vídeos

| Regra | Descrição |
|-------|-----------|
| **Step isolado** | Cada vídeo = 1 step exclusivo |
| **Roteiro interno** | Criar arquivo `.md` com roteiro (não exibir) |
| **Placeholder** | Usar URL placeholder até ter vídeo final |
| **Confirmação** | Sempre aguardar "assisti" antes de avançar |

### 5.4 Escolhas e Bifurcações

| Regra | Descrição |
|-------|-----------|
| **Máximo 2-3 opções** | Evitar muitas escolhas simultâneas |
| **Descrição clara** | Cada opção com descrição concisa |
| **Sem julgamento** | Ambas opções são válidas pedagogicamente |
| **Pausa antes** | Incluir pausa intencional antes da escolha |

---

## 6. Formato dos Arquivos de Conteúdo

### 6.1 Template: Apresentação (`apresentacao.md`)

```markdown
# Apresentação da Trilha

**Ícones Integrados**
- 🟡 Eu compreendo!
- 🟡 Eu proponho!
- 🟡 Eu reflito!

**Pilares Integrados**
- 🌱 **[Nome do Pilar 1]**: [Descrição do pilar]
- ☀️ **[Nome do Pilar 2]**: [Descrição do pilar]

---

[Texto de boas-vindas e introdução ao tema da trilha]

[Descrição do objetivo da trilha]

[Visão geral do que será abordado]
```

### 6.2 Template: Texto de Abertura (`texto_abertura.md`)

```markdown
# Texto de Abertura

[Contextualização do tema]

[Desafios ou problemas a serem abordados]

[Convite à reflexão]

Vamos começar?
```

### 6.3 Template: Texto de Articulação (`texto_articulacao.md`)

```markdown
# Texto de Articulação

[Conexão entre teoria e prática]

[Explicação das competências]

[Como as competências se aplicam na sala de aula]

---

[Convite para as perguntas reflexivas]
```

### 6.4 Template: Texto Complementar (`texto_complementar.md`)

```markdown
# Texto Complementar

[Aprofundamento do tema]

[Conexão com o vídeo/situação-problema]

[Convite para reflexão]

---

[Transição para próxima etapa]
```

### 6.5 Template: Conclusão (`conclusao.md`)

```markdown
# Conclusão

[Síntese dos principais pontos]

[Conexão com os fundamentos da prática pedagógica]:
- [Pilar 1]
- [Pilar 2]
- [Pilar 3]
- [Pilar 4]

[Mensagem motivacional]

---

Parabéns por concluir o Trilho [XX]!

[Mensagem de encerramento e próximos passos]
```

### 6.6 Template: Roteiro de Vídeo (`videoXX.md`)

```markdown
# Vídeo XX — [Título do Vídeo]

[ROTEIRO DO VÍDEO: colar aqui o texto/transcrição]

**Link do roteiro original:**
[URL do documento fonte]

---

*Nota: Este arquivo contém o roteiro/transcrição do vídeo. 
O roteiro é para contexto interno e NÃO deve ser exibido ao docente.*

---

[Descrição breve do propósito do vídeo]
```

---

## 7. Configuração de Steps (Python)

### 7.1 Ordem dos Steps (`constants.py`)

```python
TRILHOXX_STEPS_ORDER: list[str] = [
    "tXX_s1_intro",
    "tXX_s2_video01",
    "tXX_s3_texto_abertura",
    "tXX_s4_pergunta_abertura",
    # ... demais steps na ordem
    "tXX_sN_conclusao_encerramento",
]
```

### 7.2 Configuração de cada Step (`constants.py`)

```python
STEP_CONFIGS: dict[str, StepConfig] = {
    "tXX_s1_intro": StepConfig(
        id="tXX_s1_intro",
        type=StepType.CONTENT,
        content_file="apresentacao.md",
        has_question=True,
        question="Você leciona para qual etapa? Anos Iniciais ou Educação Infantil?"
    ),
    "tXX_s2_video01": StepConfig(
        id="tXX_s2_video01",
        type=StepType.VIDEO,
        content_file="video01.md",
        has_question=False
    ),
    "tXX_s7_q1": StepConfig(
        id="tXX_s7_q1",
        type=StepType.QUESTION,
        has_question=True,
        question="[Texto da pergunta reflexiva]"
    ),
    # ... demais configurações
}
```

### 7.3 Rubricas de Avaliação (`constants.py`)

```python
INTERNAL_RUBRICS: dict[str, RubricCriteria] = {
    "tXX_s7_q1": RubricCriteria(
        question="[Texto da pergunta]",
        excellent="[Critério para resposta excelente]",
        good="[Critério para resposta boa]",
        developing="[Critério para resposta em desenvolvimento]",
        needs_support="[Critério para resposta que precisa de apoio]"
    ),
    # ... demais rubricas
}
```

### 7.4 Competências da Trilha (`constants.py`)

```python
TRILHOXX_COMPETENCIAS = """
**Competências da Dimensão X — [Nome da Dimensão]**

**X.1** [Descrição da competência 1]

**X.2** [Descrição da competência 2]

**X.3** [Descrição da competência 3]

**X.4** [Descrição da competência 4]
"""
```

---

## 8. Checklist de Criação

### 8.1 Antes de Começar

- [ ] Tenho o material original completo?
- [ ] Identifiquei o tema central e objetivo?
- [ ] Defini os pilares integrados?
- [ ] Listei as competências da trilha?

### 8.2 Estruturação

- [ ] Mapeei todas as seções do material original
- [ ] Defini a quantidade de steps (15-25 recomendado)
- [ ] Identifiquei os tipos de cada step
- [ ] Criei a lista de step IDs na ordem correta

### 8.3 Arquivos de Conteúdo

- [ ] Criei `apresentacao.md`
- [ ] Criei `texto_abertura.md`
- [ ] Criei `texto_articulacao.md` (se aplicável)
- [ ] Criei `texto_complementar.md` (se aplicável)
- [ ] Criei `conclusao.md`
- [ ] Criei roteiros de vídeo (`videoXX.md`)
- [ ] Criei roteiros de vídeos alternativos (`video03_*.md`)

### 8.4 Configuração Python

- [ ] Adicionei steps em `TRILHOXX_STEPS_ORDER`
- [ ] Configurei cada step em `STEP_CONFIGS`
- [ ] Criei rubricas em `INTERNAL_RUBRICS` para perguntas
- [ ] Defini `TRILHOXX_COMPETENCIAS`
- [ ] Adicionei materiais em `AVAILABLE_MATERIALS`

### 8.5 Instruções de Steps

- [ ] Criei instrução para cada step em `step_instructions.py`
- [ ] Incluí conteúdo a ser carregado nos steps de CONTENT
- [ ] Defini perguntas específicas nos steps de QUESTION
- [ ] Configurei lógica de caminhos nos steps de CHOICE

### 8.6 Validação Final

- [ ] Testei o fluxo completo da trilha
- [ ] Verifiquei transições entre steps
- [ ] Confirmei que vídeos têm placeholders/URLs
- [ ] Revisei rubricas de feedback
- [ ] Validei que nenhum material proibido é mencionado

---

## 9. Exemplo Completo: Trilho 01

### 9.1 Resumo do Trilho 01

| Atributo | Valor |
|----------|-------|
| **ID** | `trilho01` |
| **Tema** | Desenvolvimento Integral |
| **Objetivo** | Compreender os fundamentos da proposta Verbum |
| **Total de Steps** | 20 |
| **Arquivos de Conteúdo** | 9 |

### 9.2 Lista de Steps

| # | Step ID | Tipo | Arquivo |
|---|---------|------|---------|
| 1 | `t01_s1_intro` | CONTENT | `apresentacao.md` |
| 2 | `t01_s2_video01` | VIDEO | `video01.md` |
| 3 | `t01_s3_texto_abertura` | CONTENT | `texto_abertura.md` |
| 4 | `t01_s4_pergunta_abertura` | QUESTION | - |
| 5 | `t01_s5_competencias` | CONTENT | - |
| 6 | `t01_s6_texto_articulacao` | CONTENT | `texto_articulacao.md` |
| 7 | `t01_s7_q1` | QUESTION | - |
| 8 | `t01_s8_q2` | QUESTION | - |
| 9 | `t01_s9_q3` | QUESTION | - |
| 10 | `t01_s10_q4` | QUESTION | - |
| 11 | `t01_s11_q5` | QUESTION | - |
| 12 | `t01_s12_video02` | VIDEO | `video02.md` |
| 13 | `t01_s13_texto_complementar` | CONTENT | `texto_complementar.md` |
| 14 | `t01_s14_perguntas_video02` | QUESTION | - |
| 15 | `t01_s15_pausa_intencional` | PAUSE | - |
| 16 | `t01_s16_escolha_caminho` | CHOICE | - |
| 17 | `t01_s17_video03_escolhido` | VIDEO | `video03_*.md` |
| 18 | `t01_s18_video03_outro` | VIDEO | `video03_*.md` |
| 19 | `t01_s19_reflexao_caminhos` | QUESTION | - |
| 20 | `t01_s20_conclusao_encerramento` | CONTENT | `conclusao.md` |

### 9.3 Arquivos de Conteúdo

```
content/trilho01/
├── apresentacao.md           # 23 linhas
├── texto_abertura.md         # 11 linhas  
├── texto_articulacao.md      # 16 linhas
├── texto_complementar.md     # 12 linhas
├── conclusao.md              # 19 linhas
├── video01.md                # Roteiro vídeo abertura
├── video02.md                # Roteiro situação-problema
├── video03_inclusao_solidaria.md    # Roteiro caminho A
└── video03_protagonismo_ativo.md    # Roteiro caminho B
```

---

## 10. Usando o Script de Geração

### 10.1 Pré-requisitos

```bash
# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac

# Instalar dependências (se necessário)
pip install pyyaml
```

### 10.2 Criar Arquivo de Definição

Crie um arquivo YAML com a definição do trilho:

```yaml
# trilhoXX_definition.yaml
trilho_id: "trilho02"
nome: "Trilho 02 - Práticas Baseadas em Evidências"
objetivo: "Compreender e aplicar práticas pedagógicas fundamentadas em evidências científicas"

icones:
  - "🟡 Eu compreendo!"
  - "🟡 Eu proponho!"
  - "🟡 Eu reflito!"

pilares:
  - nome: "Mente sã"
    emoji: "🌱"
    descricao: "Promover autorregulação emocional, atenção plena e clareza mental"
  - nome: "Espírito pleno"
    emoji: "☀️"
    descricao: "Reforçar a dimensão vocacional, ética e espiritual do docente"

competencias:
  - id: "2.1"
    texto: "Primeira competência da dimensão"
  - id: "2.2"
    texto: "Segunda competência da dimensão"

steps:
  - id: "t02_s1_intro"
    tipo: "content"
    label: "Introdução"
    content_file: "apresentacao.md"
    has_question: true
    question: "Você leciona para qual etapa?"
    
  - id: "t02_s2_video01"
    tipo: "video"
    label: "Vídeo 01"
    content_file: "video01.md"
    video_url: "https://example.com/video01"
    
  # ... demais steps

materiais_proibidos:
  - "A Coragem de Educar"
  - "Teoria do Iceberg"
```

### 10.3 Executar o Script

```bash
python scripts/generate_trilho.py scripts/trilho02_definition.yaml
```

### 10.4 Saída Gerada

O script irá gerar:

1. **Arquivos de conteúdo** em `domain/verbum/tutor_docente/content/trilhoXX/`
2. **Configurações** atualizadas em `constants.py`
3. **Instruções** atualizadas em `step_instructions.py`
4. **Plano** em `trilhoXX_plan.py`

### 10.5 Validação

Após gerar, valide:

```bash
# Verificar se os arquivos foram criados
ls domain/verbum/tutor_docente/content/trilhoXX/

# Testar importação
python -c "from domain.verbum.tutor_docente.constants import TRILHOXX_STEPS_ORDER; print(len(TRILHOXX_STEPS_ORDER))"
```

---

## Conclusão

Este guia fornece a estrutura e os templates necessários para transformar qualquer material educacional da Verbum em uma trilha estruturada para o Tutor Docente. Seguindo as convenções e checklists apresentados, você garantirá consistência e qualidade na criação de novas trilhas.

**Lembre-se**:
- Mantenha o tom acolhedor e formativo
- Respeite os pilares e valores da Verbum
- Use apenas os materiais autorizados
- Teste o fluxo completo antes de publicar

---

*Documento criado em: Janeiro de 2026*
*Versão: 1.0*
