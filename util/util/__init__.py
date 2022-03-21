from .util import *
from .util_find_program import *
from . import reg
from . import win


def download(url, dst_file_path):
    """
    Download by url to file.
    Ignore if already exist.
    Throw exception if any error happen.
    
    Some though:
1. can I auto import packages
    """
    if os.path.exists(dst_file_path):
        print(f"already download for file: {dst_file_path}")
        return
