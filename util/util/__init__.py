import os
from .util import *
from .util_find_program import *
from . import reg
from . import win


def expand_config_path(sub_folder: str) -> str:
    return os.path.abspath(os.path.expanduser(f"~/.config/{sub_folder}"))


def get_file_content(path: str) -> str:
    """
    if file is not found, return ''
    """
    if not os.path.exist(path):
        return ''
    with open(path, 'r') as f:
        return f.read()


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
