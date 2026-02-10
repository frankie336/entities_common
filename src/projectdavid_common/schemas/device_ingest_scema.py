# src/projectdavid_common/schemas/device_ingest_scema.py

from typing import List, Optional

from pydantic import BaseModel, Field, validator


class DeviceIngest(BaseModel):
    host_name: str
    ip_address: Optional[str] = None
    platform: str = Field(..., description="e.g. cisco_ios, arista_eos")
    groups: List[str] = []

    # Metadata for the UI/LLM context
    site: Optional[str] = None
    role: Optional[str] = None

    @validator('groups', pre=True)
    def ensure_list(cls, v):
        if isinstance(v, str):
            return [v]
        return v


class InventoryIngestRequest(BaseModel):
    # ✅ ADDED: The partition key for the database
    assistant_id: str = Field(..., description="The UUID of the assistant owning this inventory")

    # The SDK sends a batch of devices
    devices: List[DeviceIngest]
    clear_existing: bool = False


class InventorySearchRequest(BaseModel):
    group_name: str
