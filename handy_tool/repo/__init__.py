import argparse

from .add import add
from .pull import pull
from .remove import remove
from .remove_all import remove_all
from .repo_list import repo_list
from .status import status
from .clean import clean


def main():
    parser = argparse.ArgumentParser(description="repo util")
    init_subparser(parser)
    args = parser.parse_args()
    args.func(args)


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

    delete_parser = repo_subparser.add_parser('remove_all')
    delete_parser.set_defaults(func=remove_all)

    delete_parser = repo_subparser.add_parser('remove')
    delete_parser.add_argument('path')
    delete_parser.set_defaults(func=remove)

    pull_parser = repo_subparser.add_parser('pull')
    pull_parser.set_defaults(func=pull)

    pull_parser = repo_subparser.add_parser('clean')
    pull_parser.set_defaults(func=clean)
