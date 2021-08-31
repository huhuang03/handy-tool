import argparse
from .clean import clean
from .init import install


def main():
    parser = argparse.ArgumentParser(description="android utils")
    subparsers = parser.add_subparsers(dest='command')
    # do some boring thing
    subparsers.add_parser('clean', help='clean the cmake cache files.')
    subparsers.add_parser('c', help='clean the cmake cache files.')

    p_i = subparsers.add_parser('i', help='install 32 bit')
    p_i.add_argument('-d', dest='build_debug', action='store_true')

    args = parser.parse_args()
    command = args.command
    if command == 'clean' or command == 'c':
        clean()
    if command == 'i':
        install(args)
