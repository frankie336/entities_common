# src/entities_common/utilities.py
# Use relative imports for modules within your package.
from entities_common.utilities.identifier_service import IdentifierService
from entities_common.utilities.logging_service import LoggingUtility
from entities_common.utilities.load_appropriate_env import load_environment

class UtilsInterface:
    """
    Provides access to utility services and helpers used across the system.

    Includes:
      - IdentifierService: for generating unique IDs.
      - LoggingUtility: for structured application logging.
      - load_environment: for loading environment variables based on runtime context.
    """
    IdentifierService = IdentifierService
    LoggingUtility = LoggingUtility
    load_environment = load_environment

