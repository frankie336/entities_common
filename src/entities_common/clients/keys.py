# entities_common/clients/api_key_client.py
from typing import List, Optional
from datetime import datetime
import httpx
from entities_common.validation import ValidationInterface
from entities_common.utilities.logging_service import LoggingUtility

logger = LoggingUtility()

class APIKeyClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        self.client = httpx.Client(base_url=self.base_url, headers=headers)

    def create_api_key(
        self, user_id: str, name: str,
        expires_at: Optional[datetime] = None,
        scopes: Optional[List[str]] = None
    ) -> ValidationInterface.APIKeyRead:
        payload = {
            "user_id": user_id,
            "name": name,
            "expires_at": expires_at.isoformat() if expires_at else None,
            "scopes": scopes or []
        }
        response = self.client.post("/v1/api-keys", json=payload)
        response.raise_for_status()
        return ValidationInterface.APIKeyRead.model_validate(response.json())

    def list_api_keys(self, user_id: str) -> List[ValidationInterface.APIKeyRead]:
        response = self.client.get(f"/v1/api-keys", params={"user_id": user_id})
        response.raise_for_status()
        return [ValidationInterface.APIKeyRead.model_validate(ak) for ak in response.json()]

    def delete_api_key(self, key_id: str) -> bool:
        response = self.client.delete(f"/v1/api-keys/{key_id}")
        response.raise_for_status()
        return True

    def close(self):
        self.client.close()
