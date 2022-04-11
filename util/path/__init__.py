import argparse
import os

from psutil import users
from ..util.util import ensure_is_win
from .user_scope import user_scope
import sys


def _do_clean(arg):
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


def _do_list(arg):
    path_list, _ = user_scope.get_path()
    print('\n'.join(path_list))


def remove(arg):
    path_list = user_scope.get_path()
    for p in path_list:
        print(p)
    print(path_list)
    pass

def add(arg):
    user_scope.add_cwd_to_path()


def main():
    ensure_is_win()
    parser = argparse.ArgumentParser(description='path maintain')

    subparser = parser.add_subparsers(dest='command')
    clean_parser = subparser.add_parser('clean')
    clean_parser.set_defaults(func=_do_clean)

    list_parser = subparser.add_parser('list')
    list_parser.set_defaults(func=_do_list)

    add_parser = subparser.add_parser('add')
    add_parser.set_defaults(func=add)

    delete_parser = subparser.add_parser('delete')
    delete_parser.set_defaults(func=remove)

    args = parser.parse_args(sys.argv[1:])
    args.func(args)