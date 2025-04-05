from typing import List, Dict, Any, Optional

from pydantic import BaseModel, Field, ConfigDict

# Adjust this import path if needed
from entities_common.schemas.users import UserBase


class ThreadCreate(BaseModel):
    participant_ids: List[str] = Field(..., description="List of participant IDs")
    meta_data: Optional[Dict[str, Any]] = Field(
        default=None, description="Optional metadata for thread"
    )


class ThreadRead(BaseModel):
    id: str
    created_at: int
    meta_data: Dict[str, Any]
    object: str
    tool_resources: Dict[str, Any]

    model_config = ConfigDict(from_attributes=True)


class ThreadUpdate(BaseModel):
    participant_ids: Optional[List[str]] = Field(
        default=None, description="Updated list of participant IDs"
    )
    meta_data: Optional[Dict[str, Any]] = Field(default=None, description="Updated metadata")

    model_config = ConfigDict(from_attributes=True)


class ThreadParticipant(UserBase):
    pass


class ThreadReadDetailed(ThreadRead):
    participants: List[UserBase]

    model_config = ConfigDict(from_attributes=True)


class ThreadIds(BaseModel):
    thread_ids: List[str]

    model_config = ConfigDict(from_attributes=True)
