import os
from typing import Optional

from dotenv import load_dotenv

from entities_common.clients.actions import ActionsClient
from entities_common.clients.assistants import AssistantsClient
from entities_common.clients.files import FileClient
from entities_common.clients.messages import MessagesClient
from entities_common.clients.runs import RunsClient
from entities_common.clients.threads import ThreadsClient
from entities_common.clients.users import UsersClient
from entities_common.services.logging_service import LoggingUtility
from .clients.vectors import VectorStoreClient

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
        vector_store_host: Optional[str] = 'localhost'
    ):
        """
        Initialize the main client with configuration.
        Optionally, a configuration object can be injected to decouple from environment variables.
        """
        self.vector_store_host = vector_store_host
        self.base_url = base_url or os.getenv('ASSISTANTS_BASE_URL', 'http://localhost:9000/')
        self.api_key = api_key or os.getenv('API_KEY', 'your_api_key')

        logging_utility.info("Validation initialized with base_url: %s", self.base_url)
        self._file_client: Optional[FileClient] = None
        self._runs_client: Optional[RunsClient] = None  # Fixed line
        self._users_client: Optional[UsersClient] = None
        self._assistants_client: Optional[AssistantsClient] = None
        self._threads_client: Optional[ThreadsClient] = None
        self._messages_client: Optional[MessagesClient] = None
        self._actions_client: Optional[ActionsClient] = None
        self._vectors_client: Optional[VectorStoreClient] = None

    @property
    def assistants(self) -> AssistantsClient:
        if self._assistants_client is None:
            self._assistants_client = AssistantsClient(base_url=self.base_url, api_key=self.api_key)
        return self._assistants_client

    @property
    def threads(self) -> ThreadsClient:
        if self._threads_client is None:
            self._threads_client = ThreadsClient(base_url=self.base_url, api_key=self.api_key)
        return self._threads_client

    @property
    def messages(self) -> MessagesClient:
        if self._messages_client is None:
            self._messages_client = MessagesClient(base_url=self.base_url, api_key=self.api_key)
        return self._messages_client

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
    def actions(self) -> ActionsClient:
        if self._actions_client is None:
            self._actions_client = RunsClient(base_url=self.base_url, api_key=self.api_key)
        return self._actions_client

    @property
    def vectors(self) -> VectorStoreClient:
        if self._vectors_client is None:
            self._vectors_client = VectorStoreClient(base_url=self.base_url, api_key=self.api_key,
                                                     vector_store_host=self.vector_store_host)

        return self._vectors_client
