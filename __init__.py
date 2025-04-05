from entities_common.validation import  ValidationInterface
from entities_common.utils import UtilsInterface

__all__ = [
           'ValidationInterface',
           'UtilsInterface',

           ]

try:
    from setuptools_scm import get_version
    __version__ = get_version(root='..', relative_to=__file__)
except Exception:
    __version__ = "unknown"
