from argparse import ArgumentParser

from . import comm


def init_parser(parser: ArgumentParser):
    parser.set_defaults(func=repo_list)


def repo_list(args):
    repos = comm.get_repo_list()
    print('repos: ')
    for repo in repos:
        print(f"path: {repo['path']}, auto_commit: {repo['auto_commit'] or False}")