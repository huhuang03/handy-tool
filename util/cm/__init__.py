import pathlib
import argparse
from .clean import clean
from ..util.util_git import add_git_ignore


def _install():
    # how can we do the install?
    pathlib.Path('build32').mkdir(exist_ok=True)
    add_git_ignore('*build*/')


def main():
    parser = argparse.ArgumentParser(description="android utils")
    subparsers = parser.add_subparsers(dest='command')
    # do some boring thing
    subparsers.add_parser('clean', help='clean the cmake cache files.')
    subparsers.add_parser('c', help='clean the cmake cache files.')

    subparsers.add_parser('i', help='install 32 bit')

    args = parser.parse_args()
    command = args.command
    if command == 'clean' or command == 'c':
        clean()
    if command == 'i':
        _install()
