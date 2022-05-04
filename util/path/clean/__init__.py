import os
from ..user_scope import user_scope


def do_clean(arg):
    """
    1. clean the directory not exist
    """
    path_list = user_scope.get_path()
    begin_size = len(path_list)
    need_remove = False
    for p in path_list:
        print(p)
        if not os.path.exists(p):
            print("remove path: " + p)
            path_list.remove(p)
            need_remove = True

    if need_remove:
        user_scope.set_path(path_list)
        end_size = len(path_list)
        print(f"clean end, removed {begin_size - end_size} path")
    else:
        print("is clean")
