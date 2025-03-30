import os
from typing import List

import httpx
from dotenv import load_dotenv
from pydantic import ValidationError


from entities_common.validation import ValidationInterface

from  entities_common.services.logging_service import LoggingUtility

validation = ValidationInterface()


load_dotenv()
# Initialize logging utility
logging_utility = LoggingUtility()


class UsersClient:
    def __init__(self, base_url=os.getenv("BASE_URL"), api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.client = httpx.Client(base_url=base_url, headers={"Authorization": f"Bearer {api_key}"})
        logging_utility.info("UsersClient initialized with base_url: %s", self.base_url)

    def create_user(self, name: str) -> validation.UserRead:
        logging_utility.info("Creating user with name: %s", name)
        user_data = validation.UserCreate(name=name)
        try:
            response = self.client.post("/v1/users", json=user_data.model_dump())
            response.raise_for_status()
            created_user = response.json()
            validated_user = validation.UserRead(**created_user)
            logging_utility.info("User created successfully with id: %s", validated_user.id)
            return validated_user
        except httpx.HTTPStatusError as e:
            logging_utility.error("HTTP error occurred while creating user: %s", str(e))
            raise
        except Exception as e:
            logging_utility.error("An error occurred while creating user: %s", str(e))
            raise

    def retrieve_user(self, user_id: str) -> validation.UserRead:
        logging_utility.info("Retrieving user with id: %s", user_id)
        try:
            response = self.client.get(f"/v1/users/{user_id}")
            response.raise_for_status()
            user = response.json()
            validated_user = validation.UserRead(**user)
            logging_utility.info("User retrieved successfully")
            return validated_user
        except httpx.HTTPStatusError as e:
            logging_utility.error("HTTP error occurred while retrieving user: %s", str(e))
            raise
        except Exception as e:
            logging_utility.error("An error occurred while retrieving user: %s", str(e))
            raise

    def update_user(self, user_id: str, **updates) -> validation.UserRead:
        logging_utility.info("Updating user with id: %s", user_id)
        try:
            current_user = self.retrieve_user(user_id)
            user_data = current_user.model_dump()
            user_data.update(updates)

            validated_data = validation.UserUpdate(**user_data)  # Validate data using Pydantic model
            response = self.client.put(f"/v1/users/{user_id}", json=validated_data.model_dump(exclude_unset=True))
            response.raise_for_status()
            updated_user = response.json()
            validated_response = validation.UserRead(**updated_user)  # Validate response using Pydantic model
            logging_utility.info("User updated successfully")
            return validated_response
        except ValidationError as e:
            logging_utility.error("Validation error: %s", e.json())
            raise ValueError(f"Validation error: {e}")
        except httpx.HTTPStatusError as e:
            logging_utility.error("HTTP error occurred while updating user: %s", str(e))
            raise
        except Exception as e:
            logging_utility.error("An error occurred while updating user: %s", str(e))
            raise

    def delete_user(self, user_id: str) -> validation.UserDeleteResponse:
        logging_utility.info("Deleting user with id: %s", user_id)
        try:
            response = self.client.delete(f"/v1/users/{user_id}")
            response.raise_for_status()
            result = response.json()
            validated_result = validation.UserDeleteResponse(**result)
            logging_utility.info("User deleted successfully")
            return validated_result
        except httpx.HTTPStatusError as e:
            logging_utility.error("HTTP error occurred while deleting user: %s", str(e))
            raise
        except Exception as e:
            logging_utility.error("An error occurred while deleting user: %s", str(e))
            raise

    def list_assistants_by_user(self, user_id: str) -> List[validation.AssistantRead]:
        logging_utility.info("Retrieving assistants for user with id: %s", user_id)
        try:
            response = self.client.get(f"/v1/users/{user_id}/assistants")
            response.raise_for_status()
            assistants = response.json()
            validated_assistants = [validation.AssistantRead(**assistant) for assistant in assistants]
            logging_utility.info("Assistants retrieved successfully for user id: %s", user_id)
            return validated_assistants
        except httpx.HTTPStatusError as e:
            logging_utility.error("HTTP error occurred while retrieving assistants: %s", str(e))
            raise
        except Exception as e:
            logging_utility.error("An error occurred while retrieving assistants: %s", str(e))
            raise


