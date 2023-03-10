import argparse
from .clean import clean
from .install import install


def main():
    parser = argparse.ArgumentParser(description="android utils")
    subparsers = parser.add_subparsers(dest='command')
    # do some boring thing
    subparsers.add_parser('clean', help='clean the cmake cache files.')
    subparsers.add_parser('c', help='clean the cmake cache files.')

    p_i = subparsers.add_parser('i', help='install 32 bit')
    p_i.add_argument('-i32', dest='install_32', action='store_true')
    p_i.add_argument('-i64', dest='install_64', action='store_true')

    args = parser.parse_args()
    command = args.command
    if command == 'clean' or command == 'c':
        clean()
    if command == 'i':
        install(args)
