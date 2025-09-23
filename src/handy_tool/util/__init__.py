from .bcolors import bcolors
from .util import *
from .util_os import *
from .util_find_program import *


def expand_config_path(sub_folder: str) -> str:
    return os.path.abspath(os.path.expanduser(f"~/.config/{sub_folder}"))


def write_file_content(path: str, content: str):
    dir_name = os.path.dirname(path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with open(path, 'w') as f:
        f.write(content)


def get_file_content(path: str) -> str:
    """
    if file is not found, return ''
    """
    if not os.path.exists(path):
        return ''
    with open(path, 'r') as f:
        return f.read()


def print_green(msg):
    print(f"{bcolors.OKGREEN}{msg}{bcolors.ENDC}")


def print_red(msg):
    print(f"{bcolors.FAIL}{msg}{bcolors.ENDC}")
