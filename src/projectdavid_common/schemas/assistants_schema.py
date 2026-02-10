# src/projectdavid_common/schemas/assistants_schema.py
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from projectdavid_common.schemas.vectors_schema import VectorStoreRead


# ───────────────────────────────────────────────
#  ASSISTANT  •  CREATE
# ───────────────────────────────────────────────
class AssistantCreate(BaseModel):
    id: Optional[str] = Field(None, description="Optional pre-generated assistant ID.")

    # ─── core info ────────────────────────────
    name: str = Field(..., description="Assistant name")
    description: str = Field("", description="Brief description")
    model: str = Field(..., description="LLM model ID")
    instructions: str = Field("", description="System instructions")

    # ─── tools & resources ────────────────────
    tools: Optional[List[dict]] = Field(None, description="OpenAI-style tool specs (dicts).")
    tool_resources: Optional[Dict[str, Dict[str, Any]]] = None

    # ─── misc settings ────────────────────────
    meta_data: Optional[dict] = None
    top_p: float = Field(1.0, ge=0, le=1)
    temperature: float = Field(1.0, ge=0, le=2)
    response_format: str = Field("auto")

    # ─── agentic settings (Level 3) ───────────
    max_turns: int = Field(
        1, ge=1, description="Max iterations. 1 = Standard, >1 = Autonomous loops."
    )
    agent_mode: bool = Field(
        False, description="False = Standard (Level 2), True = Autonomous (Level 3)."
    )
    # NEW: Web Access toggle
    web_access: bool = Field(False, description="Enable live web search and browsing capabilities.")
    decision_telemetry: bool = Field(
        False, description="Enable detailed reasoning/confidence logging."
    )

    # ─── webhooks ─────────────────────────────
    webhook_url: Optional[HttpUrl] = None
    webhook_secret: Optional[str] = Field(None, min_length=16)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Search Assistant",
                "model": "gpt-4o-mini",
                "agent_mode": True,
                "web_access": True,  # Example update
                "decision_telemetry": True,
                "tool_resources": {"file_search": {"vector_store_ids": ["vs_docs"]}},
            }
        }
    )


# ───────────────────────────────────────────────
#  ASSISTANT  •  READ
# ───────────────────────────────────────────────
class AssistantRead(BaseModel):
    id: str
    user_id: Optional[str] = None
    object: str
    created_at: int

    name: str
    description: Optional[str] = None
    model: str
    instructions: Optional[str] = None

    tools: Optional[List[dict]] = None
    tool_resources: Optional[Dict[str, Dict[str, Any]]] = None

    meta_data: Optional[Dict[str, Any]] = None
    top_p: float
    temperature: float
    response_format: str

    # ─── agentic settings ─────────────────────
    max_turns: int
    agent_mode: bool
    web_access: bool  # NEW
    decision_telemetry: bool

    vector_stores: List[VectorStoreRead] = Field(default_factory=list)
    webhook_url: Optional[HttpUrl] = None

    model_config = ConfigDict(from_attributes=True)


# ───────────────────────────────────────────────
#  ASSISTANT  •  UPDATE  (patched)
# ───────────────────────────────────────────────
class AssistantUpdate(BaseModel):
    # ─── scalar fields ────────────────────────
    name: Optional[str] = None
    description: Optional[str] = None
    model: Optional[str] = None
    instructions: Optional[str] = None
    meta_data: Optional[Dict[str, Any]] = None
    top_p: Optional[float] = Field(None, ge=0, le=1)
    temperature: Optional[float] = Field(None, ge=0, le=2)
    response_format: Optional[str] = None

    # ─── agentic settings ─────────────────────
    max_turns: Optional[int] = Field(None, ge=1)
    agent_mode: Optional[bool] = None
    web_access: Optional[bool] = None  # NEW
    decision_telemetry: Optional[bool] = None

    # ─── relationship IDs (lists of strings) ──
    tools: Optional[List[dict]] = Field(None, description="OpenAI-style tool specs (dicts).")
    users: Optional[List[str]] = None
    vector_stores: Optional[List[str]] = None

    # ─── JSON config ─────────────────────────
    tool_resources: Optional[Dict[str, Dict[str, Any]]] = None

    # ─── webhooks ─────────────────────────────
    webhook_url: Optional[HttpUrl] = None
    webhook_secret: Optional[str] = Field(None, min_length=16)

    # forbid unknown keys so stray dicts can’t sneak in
    model_config = ConfigDict(extra="forbid")
