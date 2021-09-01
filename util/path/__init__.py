import argparse
from ..util.util import ensure_is_win
from .user_scope import user_scope


def _do_clean():
    path_list, _ = user_scope.get_path()
    path_list = [p.strip('\\') for p in path_list]
    path_list = list(dict.fromkeys(path_list))
    print(path_list)


def main():
    ensure_is_win()
    parser = argparse.ArgumentParser(description='path maintain')
    subparser = parser.add_subparsers(dest='command')
    subparser.add_parser('clean')
    args = parser.parse_args()
    if args.command == 'clean':
        _do_clean()