import argparse
import os
import sys

from . import util as util_path
from .clean import do_clean
from .user_scope import user_scope
from ..util import reg
from ..util.util import ensure_is_win
from . import list as _list


def remove(arg):
    path_list = user_scope.get_path()
    for p in path_list:
        print(p)
    print(path_list)
    pass


def add(arg):
    path_list = util_path.get_path_list()
    path_list = [util_path.format_path(p) for p in path_list]

    # do deduplication manually
    dedup_path_list = []
    for p in path_list:
        if p not in dedup_path_list:
            dedup_path_list.append(p)
    path_list = dedup_path_list
    print(f'path_list: {path_list}')

    to_add_path = os.getcwd()
    if to_add_path in path_list:
        print("already exist in path")
        return
    path_list.append(to_add_path)
    reg.set_env_value("Path", ";".join(path_list))
    print('done')


def main():
    ensure_is_win()
    parser = argparse.ArgumentParser(description='path maintain')

    subparser = parser.add_subparsers(dest='command')
    clean_parser = subparser.add_parser('clean')
    clean_parser.set_defaults(func=do_clean)

    list_parser = subparser.add_parser('list')
    _list.init_parser(list_parser)

    add_parser = subparser.add_parser('add')
    add_parser.set_defaults(func=add)

    delete_parser = subparser.add_parser('delete')
    delete_parser.set_defaults(func=remove)

    args = parser.parse_args(sys.argv[1:])
    args.func(args)
