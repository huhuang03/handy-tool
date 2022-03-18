from .util import *
from .util_find_program import *
from . import reg
from . import win


def donwload(url, dst_file_path):
    """
    Ignore if already exist
    """
    if os.path.exists(dst_file_path):
        print(f"already donwload for file: {dst_file_path}")