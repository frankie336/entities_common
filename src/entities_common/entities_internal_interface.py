import os
from typing import Any, Dict, Optional

from dotenv import load_dotenv

from .clients.files import FileClient
from .clients.runs import RunsClient

from .services.logging_service import LoggingUtility

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
        self._runs_client = Optional[RunsClient] = None



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
