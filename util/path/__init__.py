import argparse
import sys

from .clean import do_clean
from .user_scope import user_scope
from ..util.util import ensure_is_win


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
    clean_parser.set_defaults(func=do_clean)

    list_parser = subparser.add_parser('list')
    list_parser.set_defaults(func=_do_list)

    add_parser = subparser.add_parser('add')
    add_parser.set_defaults(func=add)

    delete_parser = subparser.add_parser('delete')
    delete_parser.set_defaults(func=remove)

    args = parser.parse_args(sys.argv[1:])
    args.func(args)