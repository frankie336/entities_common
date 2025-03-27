# src/entities_common/utilities.py
# Use relative imports for modules within your package.
from entities_common.utilities.identifier_service import IdentifierService
from entities_common.utilities.logging_service import LoggingUtility


class UtilsInterface:
    """
    Exposes Pydantic validation classes, retaining their original naming.

    This interface allows consumers to access the various schemas like:
      - ValidationInterface.FileUploadRequest
      - ValidationInterface.ActionCreate
      - etc.
    """
    IdentifierService = IdentifierService
    LoggingUtility = LoggingUtility
