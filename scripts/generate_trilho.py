#!/usr/bin/env python3
"""
Script para gerar automaticamente a estrutura de um trilho a partir de uma definição YAML.

Uso:
    python scripts/generate_trilho.py <arquivo_definicao.yaml> [--output-dir <dir>] [--dry-run]

Exemplo:
    python scripts/generate_trilho.py scripts/trilho02_definition.yaml
    python scripts/generate_trilho.py scripts/trilho02_definition.yaml --dry-run
"""

import argparse
import sys
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field

# Tentar importar yaml, com fallback para instalação
try:
    import yaml
except ImportError:
    print("Erro: PyYAML não está instalado.")
    print("Execute: pip install pyyaml")
    sys.exit(1)


# ══════════════════════════════════════════════════════════════
# Estruturas de Dados
# ══════════════════════════════════════════════════════════════

@dataclass
class Pilar:
    """Representa um pilar da trilha."""
    nome: str
    emoji: str
    descricao: str


@dataclass
class Competencia:
    """Representa uma competência da trilha."""
    id: str
    texto: str


@dataclass
class Rubrica:
    """Representa uma rubrica de avaliação."""
    question: str
    excellent: str = ""
    good: str = ""
    developing: str = ""
    needs_support: str = ""


@dataclass
class StepDefinition:
    """Definição de um step."""
    id: str
    tipo: str  # content, video, question, choice, pause
    label: str
    content_file: str | None = None
    has_question: bool = False
    question: str | None = None
    video_url: str | None = None
    rubrica: Rubrica | None = None
    # Para steps de pergunta em série
    question_number: int | None = None
    total_questions: int | None = None
    # Para steps de escolha
    opcoes: list[dict] = field(default_factory=list)
    # Conteúdo inline (se não tiver arquivo)
    content_inline: str | None = None


@dataclass
class TrilhoDefinition:
    """Definição completa de um trilho."""
    trilho_id: str
    nome: str
    objetivo: str
    icones: list[str]
    pilares: list[Pilar]
    competencias: list[Competencia]
    steps: list[StepDefinition]
    materiais_proibidos: list[str] = field(default_factory=list)
    
    @property
    def trilho_number(self) -> str:
        """Extrai o número do trilho (ex: 'trilho01' -> '01')."""
        return self.trilho_id.replace("trilho", "")
    
    @property
    def prefix(self) -> str:
        """Prefixo para step IDs (ex: 't01')."""
        return f"t{self.trilho_number}"


# ══════════════════════════════════════════════════════════════
# Parser YAML
# ══════════════════════════════════════════════════════════════

def parse_yaml(filepath: Path) -> TrilhoDefinition:
    """Lê e parseia o arquivo YAML de definição."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    # Parsear pilares
    pilares = []
    for p in data.get("pilares", []):
        pilares.append(Pilar(
            nome=p["nome"],
            emoji=p.get("emoji", "🔹"),
            descricao=p["descricao"]
        ))
    
    # Parsear competências
    competencias = []
    for c in data.get("competencias", []):
        competencias.append(Competencia(
            id=c["id"],
            texto=c["texto"]
        ))
    
    # Parsear steps
    steps = []
    for s in data.get("steps", []):
        rubrica = None
        if "rubrica" in s:
            r = s["rubrica"]
            rubrica = Rubrica(
                question=r.get("question", s.get("question", "")),
                excellent=r.get("excellent", ""),
                good=r.get("good", ""),
                developing=r.get("developing", ""),
                needs_support=r.get("needs_support", "")
            )
        
        steps.append(StepDefinition(
            id=s["id"],
            tipo=s["tipo"],
            label=s.get("label", s["id"]),
            content_file=s.get("content_file"),
            has_question=s.get("has_question", False),
            question=s.get("question"),
            video_url=s.get("video_url"),
            rubrica=rubrica,
            question_number=s.get("question_number"),
            total_questions=s.get("total_questions"),
            opcoes=s.get("opcoes", []),
            content_inline=s.get("content_inline")
        ))
    
    return TrilhoDefinition(
        trilho_id=data["trilho_id"],
        nome=data["nome"],
        objetivo=data["objetivo"],
        icones=data.get("icones", []),
        pilares=pilares,
        competencias=competencias,
        steps=steps,
        materiais_proibidos=data.get("materiais_proibidos", [])
    )


# ══════════════════════════════════════════════════════════════
# Geradores de Conteúdo
# ══════════════════════════════════════════════════════════════

def generate_apresentacao(trilho: TrilhoDefinition, content_inline: str | None = None) -> str:
    """Gera o arquivo apresentacao.md."""
    if content_inline:
        return content_inline
    
    icones_text = "\n".join(f"- {i}" for i in trilho.icones)
    pilares_text = "\n".join(
        f"- {p.emoji} **{p.nome}**: {p.descricao}" 
        for p in trilho.pilares
    )
    
    return f"""# Apresentação da Trilha

**Ícones Integrados**
{icones_text}

**Pilares Integrados**
{pilares_text}

---

{trilho.objetivo}

Ao longo desta trilha, você será convidado a refletir sobre sua prática docente e descobrir novas estratégias para aplicar em sala de aula.
"""


def generate_conclusao(trilho: TrilhoDefinition, content_inline: str | None = None) -> str:
    """Gera o arquivo conclusao.md."""
    if content_inline:
        return content_inline
    
    num = trilho.trilho_number
    return f"""# Conclusão

Sua prática docente envolve dilemas e decisões que exigem equilíbrio e intencionalidade.

Cada decisão que você toma precisa expressar intencionalidade e estar conectada aos fundamentos da sua prática pedagógica:

- Promover o desenvolvimento integral dos estudantes
- Aplicar práticas baseadas em evidências
- Articular currículo, avaliação e recursos com coerência pedagógica
- Integrar valores cristãos como solidariedade, justiça e propósito

---

Parabéns por concluir o Trilho {num}!

Você deu um passo importante na sua formação docente. Continue aplicando essas reflexões em sua prática diária.
"""


def generate_texto_template(titulo: str, content_inline: str | None = None) -> str:
    """Gera um arquivo de texto genérico."""
    if content_inline:
        return content_inline
    
    return f"""# {titulo}

[Conteúdo a ser preenchido]

---

Vamos continuar?
"""


def generate_video_template(
    video_num: str, 
    titulo: str, 
    descricao: str = "",
    link_roteiro: str = "",
    content_inline: str | None = None
) -> str:
    """Gera um arquivo de roteiro de vídeo."""
    if content_inline:
        return content_inline
    
    link_section = ""
    if link_roteiro:
        link_section = f"""
**Link do roteiro original:**
{link_roteiro}
"""
    
    return f"""# Vídeo {video_num} — {titulo}

[ROTEIRO DO VÍDEO {video_num}: colar aqui o texto do documento]
{link_section}
---

*Nota: Este arquivo deve conter o roteiro/transcrição do vídeo. O roteiro é para contexto interno e NÃO deve ser exibido ao docente.*

---

{descricao}
"""


# ══════════════════════════════════════════════════════════════
# Gerador de Configurações Python
# ══════════════════════════════════════════════════════════════

def generate_constants_section(trilho: TrilhoDefinition) -> str:
    """Gera a seção de constants.py para o trilho."""
    num = trilho.trilho_number
    upper_id = trilho.trilho_id.upper().replace("TRILHO", "TRILHO")
    
    # Gerar ordem dos steps
    steps_order = ",\n    ".join(f'"{s.id}"' for s in trilho.steps)
    
    # Gerar configurações de steps
    step_configs = []
    for s in trilho.steps:
        config_parts = [
            f'        id="{s.id}"',
            f'        type=StepType.{s.tipo.upper()}',
        ]
        if s.content_file:
            config_parts.append(f'        content_file="{s.content_file}"')
        config_parts.append(f'        has_question={s.has_question}')
        if s.question:
            escaped_q = s.question.replace('"', '\\"')
            config_parts.append(f'        question="{escaped_q}"')
        
        config_str = ",\n".join(config_parts)
        step_configs.append(f'    "{s.id}": StepConfig(\n{config_str}\n    )')
    
    step_configs_str = ",\n".join(step_configs)
    
    # Gerar rubricas
    rubrics = []
    for s in trilho.steps:
        if s.rubrica:
            r = s.rubrica
            rubric_str = f'''    "{s.id}": RubricCriteria(
        question="{r.question.replace('"', '\\"')}",
        excellent="{r.excellent.replace('"', '\\"')}",
        good="{r.good.replace('"', '\\"')}",
        developing="{r.developing.replace('"', '\\"')}",
        needs_support="{r.needs_support.replace('"', '\\"')}"
    )'''
            rubrics.append(rubric_str)
    
    rubrics_str = ",\n".join(rubrics) if rubrics else "    # Adicionar rubricas conforme necessário"
    
    # Gerar competências
    comp_items = "\n\n".join(f"**{c.id}** {c.texto}" for c in trilho.competencias)
    
    # Gerar lista de materiais
    materials = [s.content_file for s in trilho.steps if s.content_file]
    materials_str = ",\n    ".join(f'"{m}"' for m in set(materials))
    
    # Gerar lista de steps apenas conteúdo
    content_only = [s.id for s in trilho.steps if s.tipo in ("video", "content", "pause") and not s.has_question]
    content_only_str = ",\n    ".join(f'"{s}"' for s in content_only)
    
    return f'''
# ══════════════════════════════════════════════════════════════
# Trilho {num} - {trilho.nome}
# ══════════════════════════════════════════════════════════════

{upper_id}_STEPS_ORDER: list[str] = [
    {steps_order},
]


# Configuração de cada Step do Trilho {num}
{upper_id}_STEP_CONFIGS: dict[str, StepConfig] = {{
{step_configs_str}
}}


# Rubricas de Avaliação do Trilho {num}
{upper_id}_INTERNAL_RUBRICS: dict[str, RubricCriteria] = {{
{rubrics_str}
}}


# Materiais Disponíveis do Trilho {num}
{upper_id}_AVAILABLE_MATERIALS: list[str] = [
    {materials_str}
]


# Steps apenas conteúdo (sem pergunta) do Trilho {num}
{upper_id}_CONTENT_ONLY_STEPS: list[str] = [
    {content_only_str}
]


# Competências do Trilho {num}
{upper_id}_COMPETENCIAS = """
**Competências da Dimensão {num}**

{comp_items}
"""
'''


# ══════════════════════════════════════════════════════════════
# Gerador de Instruções de Steps
# ══════════════════════════════════════════════════════════════

def generate_step_instruction(step: StepDefinition, trilho: TrilhoDefinition) -> str:
    """Gera a instrução para um step específico."""
    
    if step.tipo == "content":
        return _generate_content_instruction(step)
    elif step.tipo == "video":
        return _generate_video_instruction(step)
    elif step.tipo == "question":
        return _generate_question_instruction(step)
    elif step.tipo == "choice":
        return _generate_choice_instruction(step)
    elif step.tipo == "pause":
        return _generate_pause_instruction(step)
    else:
        return f"# Instrução não definida para tipo: {step.tipo}"


def _generate_content_instruction(step: StepDefinition) -> str:
    """Gera instrução para step de conteúdo."""
    question_section = ""
    if step.has_question and step.question:
        question_section = f'''

PERGUNTA DE ENGAJAMENTO (fazer ao final):
👉 "{step.question}"

Aguarde a resposta do docente antes de prosseguir.'''
    
    return f'''
═══════════════════════════════════════════════════════════════
STEP ATUAL: {step.label}
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Apresente o conteúdo em tom acolhedor e conversacional.
2. Após apresentar, verifique se há dúvidas.

CONTEÚDO A APRESENTAR:
{{content or "[Conteúdo não carregado]"}}
{question_section}

Após apresentar, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
'''


def _generate_video_instruction(step: StepDefinition) -> str:
    """Gera instrução para step de vídeo."""
    url = step.video_url or "https://example.com/video-placeholder"
    
    return f'''
═══════════════════════════════════════════════════════════════
STEP ATUAL: {step.label}
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
1. Mencione que há um vídeo para assistir.
2. Insira o iframe do vídeo: <iframe src='{url}' width='560' height='315' frameborder='0' allowfullscreen></iframe>
3. Diga: "Assista ao vídeo com atenção. Quando terminar, me avise para continuarmos."

IMPORTANTE: NÃO mostre o roteiro do vídeo. Apenas mencione o vídeo e insira o iframe.

Após o docente indicar que assistiu, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
'''


def _generate_question_instruction(step: StepDefinition) -> str:
    """Gera instrução para step de pergunta."""
    title = step.label
    if step.question_number and step.total_questions:
        title = f"Pergunta Reflexiva {step.question_number} de {step.total_questions}"
    
    return f'''
═══════════════════════════════════════════════════════════════
STEP ATUAL: {title}
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Faça a seguinte pergunta e aguarde a resposta:

👉 "{step.question or '[Pergunta não definida]'}"

Aplique o fluxo de feedback após a resposta.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
'''


def _generate_choice_instruction(step: StepDefinition) -> str:
    """Gera instrução para step de escolha."""
    opcoes_text = ""
    for i, op in enumerate(step.opcoes):
        letra = chr(65 + i)  # A, B, C...
        emoji = op.get("emoji", f"🔹")
        nome = op.get("nome", f"Opção {letra}")
        desc = op.get("descricao", "")
        opcoes_text += f"\n**{emoji} Caminho {nome}:**\n'{desc}'\n"
    
    if not opcoes_text:
        opcoes_text = """
**🅰️ Caminho A:**
'[Descrição da opção A]'

**🅱️ Caminho B:**
'[Descrição da opção B]'
"""
    
    return f'''
═══════════════════════════════════════════════════════════════
STEP ATUAL: {step.label}
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Apresente os caminhos possíveis e peça que o docente escolha:

"Não existe um caminho único ou perfeito. Cada escolha traz vantagens e limites.

É hora de se colocar como protagonista. Escolha um dos caminhos:
{opcoes_text}
👉 Qual caminho você escolhe?"

IMPORTANTE: Registre a escolha para os próximos steps.

Após a escolha, faça uma pergunta de reflexão sobre os benefícios e riscos da escolha.

Depois do feedback, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
'''


def _generate_pause_instruction(step: StepDefinition) -> str:
    """Gera instrução para step de pausa."""
    return f'''
═══════════════════════════════════════════════════════════════
STEP ATUAL: {step.label}
═══════════════════════════════════════════════════════════════

INSTRUÇÃO:
Conduza uma pausa guiada de reflexão:

"Faça uma pausa intencional. Esse momento é para você se colocar no lugar 
do docente diante do desafio apresentado.

Projete como você enfrentaria esse desafio em sua própria sala de aula.

Respire fundo. Quando estiver pronto(a), me avise para continuarmos."

Após o docente indicar que está pronto, pergunte:
👉 "Você tem alguma dúvida sobre esta etapa ou podemos prosseguir para a próxima?"
'''


def generate_step_instructions_file(trilho: TrilhoDefinition) -> str:
    """Gera o arquivo step_instructions.py para o trilho."""
    num = trilho.trilho_number
    upper_id = trilho.trilho_id.upper()
    
    # Gerar labels
    labels = ",\n    ".join(f'"{s.id}": "{s.label}"' for s in trilho.steps)
    
    # Gerar funções de instrução
    instructions_map = []
    function_defs = []
    
    for s in trilho.steps:
        func_name = f"_get_{s.id.replace(trilho.prefix + '_', '')}_instruction"
        instruction = generate_step_instruction(s, trilho)
        
        # Determinar se precisa de parâmetro content
        needs_content = s.tipo == "content" and s.content_file
        needs_caminho = "video03" in s.id or s.tipo == "choice"
        
        params = []
        if needs_content:
            params.append("content: Optional[str] = None")
        if needs_caminho:
            params.append("caminho: Optional[str] = None")
        
        params_str = ", ".join(params) if params else ""
        
        # Escapar aspas triplas na instrução
        instruction_escaped = instruction.replace('"""', "'''")
        
        func_def = f'''
def {func_name}({params_str}) -> str:
    return f"""{instruction_escaped}"""
'''
        function_defs.append(func_def)
        
        # Mapear para o dicionário
        call_params = []
        if needs_content:
            call_params.append("content")
        if needs_caminho:
            call_params.append("caminho")
        call_str = ", ".join(call_params)
        
        instructions_map.append(f'        "{s.id}": {func_name}({call_str})')
    
    instructions_map_str = ",\n".join(instructions_map)
    function_defs_str = "\n".join(function_defs)
    
    return f'''"""
Instruções específicas para cada step do Trilho {num}.
Gerado automaticamente pelo script generate_trilho.py
"""

from typing import Optional


# Labels amigáveis para cada step
{upper_id}_STEP_LABELS: dict[str, str] = {{
    {labels}
}}


def get_{trilho.trilho_id}_step_instruction(step_id: str, content: Optional[str] = None, caminho: Optional[str] = None) -> str:
    """
    Retorna a instrução específica para um step do Trilho {num}.
    
    Args:
        step_id: ID do step
        content: Conteúdo carregado do arquivo .md (se houver)
        caminho: Caminho escolhido pelo docente (A ou B)
    
    Returns:
        Instrução formatada para o step.
    """
    instructions = {{
{instructions_map_str}
    }}
    
    return instructions.get(step_id, f"[Step não encontrado: {{step_id}}]")

{function_defs_str}
'''


# ══════════════════════════════════════════════════════════════
# Gerador do Plano do Trilho
# ══════════════════════════════════════════════════════════════

def generate_trilho_plan(trilho: TrilhoDefinition) -> str:
    """Gera o arquivo trilhoXX_plan.py."""
    num = trilho.trilho_number
    
    # Gerar lista de materiais
    materials = [s.content_file for s in trilho.steps if s.content_file]
    materials_str = "\n".join(f"- {m}" for m in set(materials))
    
    # Gerar sequência de steps
    steps_sequence = "\n".join(f"{i+1}) {s.label}" for i, s in enumerate(trilho.steps))
    
    # Gerar lista de proibidos
    proibidos = "\n".join(f'- "{p}"' for p in trilho.materiais_proibidos)
    if not proibidos:
        proibidos = "- Qualquer material não listado acima"
    
    # Pilares
    pilares_str = "\n".join(f"{p.emoji} {p.nome} — {p.descricao}" for p in trilho.pilares)
    
    # Ícones
    icones_str = " | ".join(trilho.icones)
    
    return f'''"""
Trilho {num} Plan - Definição do plano e contexto do trilho.
Gerado automaticamente pelo script generate_trilho.py
"""

{trilho.trilho_id.upper()}_PLAN_PROMPT = """
═══════════════════════════════════════════════════════════════
TRILHO {num}: {trilho.nome}
═══════════════════════════════════════════════════════════════

OBJETIVO
{trilho.objetivo}

ÍCONES INTEGRADOS
{icones_str}

PILARES INTEGRADOS
{pilares_str}

SEQUÊNCIA OBRIGATÓRIA DO TRILHO
{steps_sequence}

REGRAS DO TRILHO
- Siga rigorosamente a ordem dos steps. NUNCA retorne a steps anteriores.
- NUNCA apresente conteúdo de um step que já foi completado, a menos que seja explicitamente solicitado pelo docente.
- NUNCA mencione materiais, vídeos, textos ou referências que não constem nos arquivos fornecidos.
- Não revele gabaritos ou rótulos de avaliação.
- Apresente conteúdo e faça perguntas conforme definido em cada step.
- Mantenha tom acolhedor e formativo em todas as interações.
- Se o docente perguntar sobre algo que não está no material, acolha e redirecione para o conteúdo da trilha.

MATERIAIS DISPONÍVEIS (use APENAS estes):
{materials_str}

PROIBIDO mencionar:
{proibidos}
"""
'''


# ══════════════════════════════════════════════════════════════
# Gerador Principal
# ══════════════════════════════════════════════════════════════

class TrilhoGenerator:
    """Gerador de estrutura de trilho."""
    
    def __init__(self, trilho: TrilhoDefinition, output_dir: Path, dry_run: bool = False):
        self.trilho = trilho
        self.output_dir = output_dir
        self.dry_run = dry_run
        self.content_dir = output_dir / "domain" / "verbum" / "tutor_docente" / "content" / trilho.trilho_id
        self.prompts_dir = output_dir / "domain" / "verbum" / "tutor_docente" / "prompts"
    
    def generate(self) -> dict[str, str]:
        """Gera todos os arquivos do trilho."""
        generated_files: dict[str, str] = {}
        
        # 1. Criar diretório de conteúdo
        if not self.dry_run:
            self.content_dir.mkdir(parents=True, exist_ok=True)
        
        # 2. Gerar arquivos de conteúdo
        generated_files.update(self._generate_content_files())
        
        # 3. Gerar configurações (constants section)
        constants_content = generate_constants_section(self.trilho)
        constants_path = self.output_dir / "generated" / f"{self.trilho.trilho_id}_constants.py"
        generated_files[str(constants_path)] = constants_content
        
        # 4. Gerar instruções de steps
        instructions_content = generate_step_instructions_file(self.trilho)
        instructions_path = self.output_dir / "generated" / f"{self.trilho.trilho_id}_step_instructions.py"
        generated_files[str(instructions_path)] = instructions_content
        
        # 5. Gerar plano do trilho
        plan_content = generate_trilho_plan(self.trilho)
        plan_path = self.prompts_dir / f"{self.trilho.trilho_id}_plan.py"
        generated_files[str(plan_path)] = plan_content
        
        # Escrever arquivos se não for dry run
        if not self.dry_run:
            # Criar diretório generated
            (self.output_dir / "generated").mkdir(exist_ok=True)
            
            for filepath, content in generated_files.items():
                path = Path(filepath)
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  [OK] Criado: {path.relative_to(self.output_dir)}")
        
        return generated_files
    
    def _generate_content_files(self) -> dict[str, str]:
        """Gera os arquivos de conteúdo (.md)."""
        files: dict[str, str] = {}
        
        # Mapear arquivos únicos
        content_files = set(s.content_file for s in self.trilho.steps if s.content_file)
        
        for filename in content_files:
            filepath = self.content_dir / filename
            
            # Encontrar step que usa esse arquivo
            step = next((s for s in self.trilho.steps if s.content_file == filename), None)
            content_inline = step.content_inline if step else None
            
            if filename == "apresentacao.md":
                content = generate_apresentacao(self.trilho, content_inline)
            elif filename == "conclusao.md":
                content = generate_conclusao(self.trilho, content_inline)
            elif filename.startswith("video"):
                # Extrair número do vídeo
                video_num = filename.replace("video", "").replace(".md", "").split("_")[0]
                titulo = step.label if step else f"Vídeo {video_num}"
                content = generate_video_template(video_num, titulo, content_inline=content_inline)
            else:
                # Texto genérico
                titulo = filename.replace(".md", "").replace("_", " ").title()
                content = generate_texto_template(titulo, content_inline)
            
            files[str(filepath)] = content
        
        return files
    
    def print_summary(self):
        """Imprime resumo da geração."""
        print(f"\n{'='*60}")
        print(f"TRILHO: {self.trilho.nome}")
        print(f"ID: {self.trilho.trilho_id}")
        print(f"{'='*60}")
        print(f"\nTotal de Steps: {len(self.trilho.steps)}")
        
        # Contar por tipo
        tipos = {}
        for s in self.trilho.steps:
            tipos[s.tipo] = tipos.get(s.tipo, 0) + 1
        
        print("\nSteps por tipo:")
        for tipo, count in sorted(tipos.items()):
            print(f"  - {tipo.upper()}: {count}")
        
        # Arquivos de conteúdo
        content_files = set(s.content_file for s in self.trilho.steps if s.content_file)
        print(f"\nArquivos de conteúdo: {len(content_files)}")
        for f in sorted(content_files):
            print(f"  - {f}")
        
        print(f"\n{'='*60}\n")


# ══════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Gera estrutura de trilho a partir de definição YAML"
    )
    parser.add_argument(
        "definition_file",
        type=Path,
        help="Arquivo YAML com a definição do trilho"
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=Path("."),
        help="Diretório de saída (default: diretório atual)"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Não criar arquivos, apenas mostrar o que seria gerado"
    )
    
    args = parser.parse_args()
    
    # Verificar se arquivo existe
    if not args.definition_file.exists():
        print(f"Erro: Arquivo não encontrado: {args.definition_file}")
        sys.exit(1)
    
    # Parsear definição
    print(f"Lendo definição: {args.definition_file}")
    trilho = parse_yaml(args.definition_file)
    
    # Criar gerador
    generator = TrilhoGenerator(trilho, args.output_dir, args.dry_run)
    
    # Mostrar resumo
    generator.print_summary()
    
    # Gerar arquivos
    if args.dry_run:
        print("MODO DRY-RUN: Nenhum arquivo será criado\n")
    
    print("Gerando arquivos...")
    files = generator.generate()
    
    if args.dry_run:
        print("\nArquivos que seriam criados:")
        for filepath in sorted(files.keys()):
            rel_path = Path(filepath).relative_to(args.output_dir) if args.output_dir != Path(".") else filepath
            print(f"  - {rel_path}")
    
    print(f"\n[OK] Geracao concluida! {len(files)} arquivos {'seriam criados' if args.dry_run else 'criados'}.")


if __name__ == "__main__":
    main()
