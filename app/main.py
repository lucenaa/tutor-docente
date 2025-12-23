"""
Verbum Tutor - Backend FastAPI
Trilho 01: Desenvolvimento Integral | Situação-Problema
"""

import os
from typing import List, Literal, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from dotenv import load_dotenv

try:
    import google.generativeai as genai
except Exception:  # pragma: no cover
    genai = None

# Importar prompts e helpers
from prompts import (
    GLOBAL_POLICY_PROMPT,
    TRILHO_01_PLAN_PROMPT,
    TRILHO01_STEPS_ORDER,
    get_next_step,
    get_step_context,
)
from prompts.trilho01_plan import is_valid_step

load_dotenv()

app = FastAPI(title="Verbum Tutor - Trilho 01")


def _normalize_origin(origin: str) -> str:
    v = origin.strip()
    if v.endswith("/"):
        v = v[:-1]
    return v


# CORS (dev + produção via env FRONTEND_ORIGIN ou FRONTEND_ORIGIN_REGEX)
allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
frontend_origin = os.environ.get("FRONTEND_ORIGIN")
if frontend_origin:
    try:
        allowed_origins.append(_normalize_origin(frontend_origin))
    except Exception:
        pass
frontend_origin_regex = os.environ.get("FRONTEND_ORIGIN_REGEX")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_origin_regex=frontend_origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ══════════════════════════════════════════════════════════════
# Models
# ══════════════════════════════════════════════════════════════


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatState(BaseModel):
    caminho_escolhido: Optional[Literal["A", "B"]] = None


class ChatPayload(BaseModel):
    lesson_id: str = "1"  # Mantido por compatibilidade, sempre "1"
    step_id: str  # Obrigatório
    messages: List[ChatMessage] = []
    state: Optional[ChatState] = None


class ChatResponse(BaseModel):
    reply: str
    step_id: str
    next_step_id: Optional[str] = None
    state: Optional[ChatState] = None


# ══════════════════════════════════════════════════════════════
# Helpers
# ══════════════════════════════════════════════════════════════


def build_system_prompt(step_id: str, state: Optional[ChatState] = None) -> str:
    """
    Constrói o system prompt completo combinando:
    1. GLOBAL_POLICY_PROMPT
    2. TRILHO_01_PLAN_PROMPT
    3. Contexto específico do step
    """
    state_dict = state.model_dump() if state else None
    step_context = get_step_context(step_id, state_dict)

    return f"""{GLOBAL_POLICY_PROMPT}

{TRILHO_01_PLAN_PROMPT}

{step_context}
"""


def detect_path_choice(message: str) -> Optional[Literal["A", "B"]]:
    """
    Detecta se o usuário escolheu caminho A ou B.
    """
    msg = message.strip().upper()
    
    # Detecção direta
    if msg in ["A", "CAMINHO A", "OPÇÃO A", "ESCOLHO A", "A)"]:
        return "A"
    if msg in ["B", "CAMINHO B", "OPÇÃO B", "ESCOLHO B", "B)"]:
        return "B"
    
    # Detecção por palavras-chave
    msg_lower = message.lower()
    if "inclusão solidária" in msg_lower or "inclusao solidaria" in msg_lower:
        return "A"
    if "protagonismo ativo" in msg_lower:
        return "B"
    
    return None


# ══════════════════════════════════════════════════════════════
# Endpoints
# ══════════════════════════════════════════════════════════════


@app.get("/")
async def healthcheck():
    return {"status": "ok", "trilho": "01", "steps": len(TRILHO01_STEPS_ORDER)}


@app.get("/api/steps")
async def get_steps():
    """Retorna a lista ordenada de steps do Trilho 01."""
    return {
        "steps": TRILHO01_STEPS_ORDER,
        "total": len(TRILHO01_STEPS_ORDER),
        "first_step": TRILHO01_STEPS_ORDER[0],
        "last_step": TRILHO01_STEPS_ORDER[-1],
    }


@app.post("/api/chat")
async def chat_api(payload: ChatPayload):
    """
    Endpoint principal de chat.
    Recebe step_id obrigatório e retorna reply + next_step_id.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GOOGLE_API_KEY não configurada.")

    if genai is None:
        raise HTTPException(
            status_code=500, detail="Biblioteca google-generativeai não instalada."
        )

    # Validar step_id
    if not is_valid_step(payload.step_id):
        raise HTTPException(
            status_code=400,
            detail=f"step_id inválido: {payload.step_id}. Steps válidos: {TRILHO01_STEPS_ORDER}",
        )

    # Gerenciar state
    state = payload.state or ChatState()

    # Detectar escolha de caminho se estiver no step de escolha
    if payload.step_id == "t01_s16_escolha_caminho" and payload.messages:
        last_user_msg = next(
            (m.content for m in reversed(payload.messages) if m.role == "user"), None
        )
        if last_user_msg:
            detected_choice = detect_path_choice(last_user_msg)
            if detected_choice:
                state.caminho_escolhido = detected_choice

    try:
        # Configurar Gemini
        genai.configure(api_key=api_key)
        model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
        
        # Construir system prompt
        system_prompt = build_system_prompt(payload.step_id, state)
        
        model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_prompt,
        )

        # Mapear histórico para o formato esperado (roles: user/model)
        contents = []
        for msg in payload.messages:
            role = "user" if msg.role == "user" else "model"
            contents.append({"role": role, "parts": [msg.content]})

        # Se não houver mensagens, iniciamos com um "Iniciar" para disparar o step
        if not contents:
            contents = [{"role": "user", "parts": ["Iniciar"]}]

        response = model.generate_content(contents=contents)
        text = getattr(response, "text", None)
        if not text:
            # Em alguns casos, a resposta vem como candidatos
            try:
                text = response.candidates[0].content.parts[0].text
            except Exception:
                text = "Não foi possível obter resposta no momento."

        # Calcular próximo step
        next_step = get_next_step(payload.step_id)

        return JSONResponse(
            {
                "reply": text,
                "step_id": payload.step_id,
                "next_step_id": next_step,
                "state": state.model_dump() if state else None,
            }
        )

    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(exc))


@app.get("/api/step/{step_id}")
async def get_step_info(step_id: str):
    """Retorna informações sobre um step específico."""
    if not is_valid_step(step_id):
        raise HTTPException(status_code=404, detail=f"Step não encontrado: {step_id}")

    from prompts.trilho01_steps import STEP_CONFIGS

    config = STEP_CONFIGS.get(step_id, {})
    next_step = get_next_step(step_id)

    return {
        "step_id": step_id,
        "type": config.get("type", "unknown"),
        "has_question": config.get("has_question", False),
        "content_file": config.get("content_file"),
        "next_step_id": next_step,
    }
