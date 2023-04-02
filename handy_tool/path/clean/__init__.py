import os
from ..util import util as util_path


def do_clean(arg):
    """
    1. clean the directory not exist
    """
    path_list = util_path.get_path_list()
    begin_size = len(path_list)
    need_remove = False
    for p in path_list:
        if not util_path.contains_env(p) and not os.path.exists(p):
            print("remove path: " + p)
            path_list.remove(p)
            need_remove = True

    if need_remove:
        end_size = len(path_list)
        print(f"clean end, removed {begin_size - end_size} path")
        print("set not impl for now")
    else:
        print("is clean")
