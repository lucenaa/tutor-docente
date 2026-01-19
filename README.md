# Tutor Docente Verbum

Agente de formação docente da Verbum Educação, desenvolvido com Google ADK (Agent Development Kit).

## Arquitetura

```
tutor-docente/
├── agent.py                    # Entry point do ADK
├── agent_factories.py          # Factory para instanciar agentes
├── pyproject.toml              # Dependências do projeto
├── core/                       # Código compartilhado
│   ├── constants.py            # Modelos AI, configurações
│   ├── exceptions.py           # Exceções customizadas
│   └── utils/                  # Utilitários
├── domain/
│   └── verbum/
│       └── tutor_docente/      # Agente Tutor Docente
│           ├── agent.py        # Root agent
│           ├── constants.py    # Steps, rubricas
│           ├── types.py        # Schemas Pydantic
│           ├── callbacks/      # Callbacks de estado
│           ├── subagents/      # Subagentes especializados
│           ├── tools/          # Tools do agente
│           ├── prompts/        # Prompts e instruções
│           └── content/        # Conteúdos das trilhas
├── web/                        # Frontend React
└── scripts/                    # Scripts de deploy
```

## Requisitos

- Python 3.11+
- Node.js 18+ (para o frontend)
- Chave de API do Google (GOOGLE_API_KEY)

## Instalação

### Backend (ADK)

```bash
# Instalar uv (gerenciador de pacotes)
pip install uv

# Instalar dependências
uv sync

# Ou com pip
pip install -e .
```

### Frontend

```bash
cd web
npm install
```

## Executando Localmente

### ADK Web Interface

```bash
# Iniciar o agente com interface web do ADK
uv run adk web domain/verbum --port 8000

# Ou especificando o agente
ADK_ENTRYPOINT=tutor_docente uv run adk web domain/verbum --port 8000
```

Acesse: http://localhost:8000

### Frontend React (alternativo)

```bash
# Terminal 1: Backend
uv run adk web domain/verbum --port 8000

# Terminal 2: Frontend
cd web
npm run dev
```

O frontend estará em http://localhost:5173

## Variáveis de Ambiente

| Variável | Descrição | Obrigatório |
|----------|-----------|-------------|
| `GOOGLE_API_KEY` | Chave da API Google Generative AI | Sim |
| `ADK_ENTRYPOINT` | Agente a carregar (default: tutor_docente) | Não |

## Estrutura do Trilho 01

O Trilho 01 "Desenvolvimento Integral" possui 20 steps:

1. Introdução e Contextualização
2. Vídeo de Abertura
3. Texto de Abertura
4. Pergunta de Reflexão Inicial
5. Competências
6. Texto de Articulação
7-11. Perguntas Reflexivas (5 perguntas)
12. Vídeo Situação-Problema
13. Texto Complementar
14. Perguntas sobre o Vídeo
15. Pausa Intencional
16. Escolha de Caminhos (A ou B)
17. Vídeo do Caminho Escolhido
18. Vídeo do Outro Caminho
19. Reflexão sobre os Caminhos
20. Conclusão e Encerramento

## Deploy

### Vertex AI (produção)

```bash
python scripts/deploy_tutor_docente.py
```

### Railway + Netlify (alternativo)

Veja o arquivo [DEPLOY.md](DEPLOY.md) para instruções detalhadas.

## Desenvolvimento

### Estrutura de um Subagente

```python
from google.adk.agents import LlmAgent
from core.constants import AIModels

subagent = LlmAgent(
    name="NomeSubagent",
    model=AIModels.GEMINI_2_5_FLASH,
    description="Descrição do subagente",
    instruction="Instruções detalhadas...",
    output_key="output_key_name",
)
```

### Adicionando um Novo Trilho

1. Criar diretório em `domain/verbum/tutor_docente/content/trilhoXX/`
2. Adicionar arquivos de conteúdo (.md)
3. Atualizar `constants.py` com steps e rubricas
4. Criar prompts em `prompts/`
5. Ajustar o agente para suportar múltiplos trilhos

## Licença

Propriedade da Verbum Educação.
