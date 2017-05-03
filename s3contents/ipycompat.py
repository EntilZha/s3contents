"""
Utilities for managing IPython 3/4 compat.

Taken from: https://github.com/quantopian/pgcontents/blob/master/pgcontents/utils/ipycompat.py
"""
import IPython

from traitlets.config import Config
from notebook.services.contents.checkpoints import (
    Checkpoints,
    GenericCheckpointsMixin,
)
from notebook.services.contents.filemanager import FileContentsManager
from notebook.services.contents.filecheckpoints import (
    GenericFileCheckpoints
)
from notebook.services.contents.manager import ContentsManager
from notebook.services.contents.tests.test_manager import (
    TestContentsManager
)
from notebook.services.contents.tests.test_contents_api import (
    APITest
)
from notebook.utils import to_os_path
from nbformat import from_dict, reads, writes
from nbformat.v4.nbbase import (
    new_code_cell,
    new_markdown_cell,
    new_notebook,
    new_raw_cell,
)
from nbformat.v4.rwbase import strip_transient
from traitlets import (
    Any,
    Bool,
    Dict,
    Instance,
    Integer,
    HasTraits,
    Unicode,
)

__all__ = [
    'APITest',
    'Any',
    'Bool',
    'Checkpoints',
    'Config',
    'ContentsManager',
    'Dict',
    'FileContentsManager',
    'GenericCheckpointsMixin',
    'GenericFileCheckpoints',
    'HasTraits',
    'Instance',
    'Integer',
    'TestContentsManager',
    'Unicode',
    'from_dict',
    'new_code_cell',
    'new_markdown_cell',
    'new_notebook',
    'new_raw_cell',
    'reads',
    'strip_transient',
    'to_os_path',
    'writes',
]
