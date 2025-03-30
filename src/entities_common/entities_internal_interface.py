import os
from typing import Any, Dict, Optional

from dotenv import load_dotenv

from entities_common.clients.files import FileClient
from entities_common.clients.runs import RunsClient
from entities_common.clients.users import UsersClient
from entities_common.clients.assistants import AssistantsClient
from entities_common.clients.threads import ThreadsClient

from entities_common.services.logging_service import LoggingUtility

# Use relative imports for modules within your package.

# Load environment variables from .env file.
load_dotenv()

# Initialize logging utility.
logging_utility = LoggingUtility()


class EntitiesInternalInterface:
    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        available_functions: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the main client with configuration.
        Optionally, a configuration object can be injected to decouple from environment variables.
        """
        self.base_url = base_url or os.getenv('ASSISTANTS_BASE_URL', 'http://localhost:9000/')
        self.api_key = api_key or os.getenv('API_KEY', 'your_api_key')

        logging_utility.info("Validation initialized with base_url: %s", self.base_url)
        self._file_client: Optional[FileClient] = None
        self._runs_client: Optional[RunsClient] = None  # Fixed line
        self._users_client: Optional[UsersClient] = None
        self._assistants_client: Optional[AssistantsClient] = None
        self._threads_client: Optional[ThreadsClient] = None

    @property
    def assistants(self) -> AssistantsClient:
        if self._assistants_client is None:
            self._assistants_client = AssistantsClient(base_url=self.base_url, api_key=self.api_key)
        return self._assistants_client

    @property
    def threads(self) -> ThreadsClient:
        if self._assistants_client is None:
            self._threads_client = ThreadsClient(base_url=self.base_url, api_key=self.api_key)
        return self._threads_client

    @property
    def users(self) -> UsersClient:
        if self._users_client is None:
            self._users_client = UsersClient(base_url=self.base_url, api_key=self.api_key)
        return self._users_client

    @property
    def runs(self) -> RunsClient:
        if self._runs_client is None:
            self._runs_client = RunsClient(base_url=self.base_url, api_key=self.api_key)
        return self._runs_client

    @property
    def files(self) -> FileClient:
        if self._file_client is None:
            self._file_client = FileClient(base_url=self.base_url, api_key=self.api_key)
        return self._file_client