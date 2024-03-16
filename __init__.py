from .node import *
from .install import *

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Show Text": ShowText
}

__all__ = ['NODE_CLASS_MAPPINGS']


