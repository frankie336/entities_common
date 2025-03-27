from entities_common.entities_internal_interface import EntitiesInternalInterface
from entities_common.validation import  ValidationInterface
from entities_common.utils.logging_service import LoggingUtility
from entities_common.utils.identifier_service import IdentifierService

__all__ = ['EntitiesInternalInterface',
           'ValidationInterface',
           'IdentifierService',
           'LoggingUtility'
           ]

try:
    from setuptools_scm import get_version
    __version__ = get_version(root='..', relative_to=__file__)
except Exception:
    __version__ = "unknown"
