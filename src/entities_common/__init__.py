# src/entities_common/__init__.py

from .entities_internal import EntitiesInternalInterface
from .validation import ValidationInterface
# Utils
from .utils import  UtilsInterface


__all__ = ['EntitiesInternalInterface',
           'ValidationInterface',
           'UtilsInterface',

           ]
