import argparse
from asyncio import subprocess
from curses import init_pair
from sqlite3 import paramstyle
from .add import add
from .repo_list import repo_list
from .status import status
from .remove import remove
from .delete import delete
from .pull import pull

def main():
    parser = argparse.ArgumentParser(description="repo util")
    init_subparser(parser)
    args = parser.parse_args()
    print(args)
    args.func(args)
    # how to run?


def init_subparser(subparser):
    """
    Initial the subparser.
    @parm subparser the result of parser.Argparser().add_subparser()
    """
    repo_subparser = subparser.add_subparsers()

    add_parser = repo_subparser.add_parser('add')
    add_parser.add_argument('--auto_commit', action="store_true")
    add_parser.set_defaults(func=add)

    list_parser = repo_subparser.add_parser('list')
    list_parser.set_defaults(func=repo_list)

    status_parser = repo_subparser.add_parser('status')
    status_parser.set_defaults(func=status)

    status_parser = repo_subparser.add_parser('st')
    status_parser.set_defaults(func=status)

    delete_parser = repo_subparser.add_parser('delete')
    delete_parser.set_defaults(func=delete)

    pull_parser = repo_subparser.add_parser('pull')
    pull_parser.set_defaults(func=pull)