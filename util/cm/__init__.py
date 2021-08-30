import os
import pathlib
import argparse
from .clean import clean
from ..util.util_git import add_git_ignore


def _install():
    # how can we do the install?
    add_git_ignore('*build*/')
    pathlib.Path('build32').mkdir(exist_ok=True)
    os.system('cd build32')
    os.system('cmake . -A win32')
    os.system('cmake --build . --config Release --target install')
    os.system('cmake --build . --config Debug --target install')
    os.system('cd ..')


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
