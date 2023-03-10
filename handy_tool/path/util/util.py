from operator import contains
from re import I
from handy_tool.util.util_find_program import find_files_iter
from ...util import reg


def get_path_list():
    path_list = reg.get_value_current_user("Environment", "Path")
    return [f for f in path_list.split(";") if f]


def _fix_path(path):
    path = path.replace('\r\n', '')
    path = path.replace('\n', '')
    return path


def format_path(path: str) -> str:
    if contains_env(path):
        print(f"find a env path: {path}")
        return path
    path = _fix_path(path)
    if path.endswith("/"):
        return path[:-1]
    return path


def contains_env(path: str) -> bool:
    find_first = path.find("%")
    if find_first < 0:
        return False
    find_second = path.find("%", find_first + 1)
    if find_second < 0:
        return False
    return True
