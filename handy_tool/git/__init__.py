import argparse

from .view import view_repo_in_browser, view_branch_in_browser


def main():
    parser = argparse.ArgumentParser(description="git util")
    subparsers = parser.add_subparsers(dest='sub_command')

    view_parser = subparsers.add_parser('view', help='view repo in browser')
    view_parser.add_argument('path', nargs="?", default="")

    args = parser.parse_args()
    if args.sub_command == 'view':
        if not args.path:
            view_repo_in_browser()
        else:
            view_branch_in_browser(args.path)