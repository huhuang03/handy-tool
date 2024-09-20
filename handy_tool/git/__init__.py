import argparse

from .view import sub_command as view_sub_command, init_sub_command as view_init_sub_command, exec as view_exec
from . import pipe
from .git_br import list_branch
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="git util")
    subparsers = parser.add_subparsers(dest='sub_command')
    view_parser = subparsers.add_parser(view_sub_command, help='view repo in browser')
    view_init_sub_command(view_parser)

    pipe_parser = subparsers.add_parser(pipe.sub_command, help='pipe command in browers')
    pipe.init_sub_command(pipe_parser)

    br = subparsers.add_parser('br', help='branch utils')
    br.add_argument('path', nargs="?", default=".")

    args = parser.parse_args()
    project_path = Path(args.path)
    if args.sub_command == 'view':
        view_exec(args)
    if args.sub_command == pipe.sub_command:
        pipe.exec(args)
    if args.sub_command == 'br':
        list_branch(project_path)