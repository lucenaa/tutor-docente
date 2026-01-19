# Prompts module for Tutor Docente
from .global_policy import GLOBAL_POLICY_PROMPT
from .trilho01_plan import TRILHO01_PLAN_PROMPT
from .step_instructions import get_step_instruction, STEP_LABELS

__all__ = [
    "GLOBAL_POLICY_PROMPT",
    "TRILHO01_PLAN_PROMPT",
    "get_step_instruction",
    "STEP_LABELS",
]
