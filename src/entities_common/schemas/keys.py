from pydantic import BaseModel, Field
from typing import Optional, List


class APIKeyRead(BaseModel):
    id: str = Field(..., description="The unique identifier for this API key")
    user_id: str = Field(..., description="User who owns the key")
    name: str = Field(..., description="Human-readable name of the key")
    created_at: int = Field(..., description="Unix timestamp of key creation")
    revoked: bool = Field(..., description="Whether the key has been revoked")
    revoked_at: Optional[int] = Field(None, description="Unix timestamp of revocation (if revoked)")


class APIKeyCreate(BaseModel):
    user_id: str = Field(..., description="ID of the user for whom the API key is being created")
    name: str = Field(..., description="Human-readable name of the API key")
    expires_at: Optional[int] = Field(
        None, description="Unix timestamp when the key will expire (optional)"
    )
    scopes: Optional[List[str]] = Field(
        None, description="A list of scopes/permissions for this API key (optional)"
    )