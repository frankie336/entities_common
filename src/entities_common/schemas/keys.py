from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class APIKeyRead(BaseModel):
    id: str = Field(..., description="The unique identifier for this API key")
    user_id: str = Field(..., description="User who owns the key")
    name: str = Field(..., description="Human-readable name of the key")
    created_at: int = Field(..., description="Unix timestamp of key creation")
    revoked: bool = Field(..., description="Whether the key has been revoked")
    revoked_at: Optional[int] = Field(
        None, description="Unix timestamp of revocation (if revoked)"
    )

    model_config = ConfigDict(from_attributes=True)
