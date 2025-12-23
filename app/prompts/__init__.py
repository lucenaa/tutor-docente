# Prompts module for Verbum Tutor
from .global_policy import GLOBAL_POLICY_PROMPT
from .trilho01_plan import TRILHO_01_PLAN_PROMPT, TRILHO01_STEPS_ORDER, get_next_step
from .trilho01_steps import get_step_context, STEP_CONFIGS

__all__ = [
    "GLOBAL_POLICY_PROMPT",
    "TRILHO_01_PLAN_PROMPT",
    "TRILHO01_STEPS_ORDER",
    "get_next_step",
    "get_step_context",
    "STEP_CONFIGS",
]

