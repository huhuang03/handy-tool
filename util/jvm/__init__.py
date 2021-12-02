from argparse import ArgumentParser
from .jvm import JVM


def main():
    _jvm: JVM = JVM()
    parser = ArgumentParser()
    subparser = parser.add_subparsers(dest="command")
    subparser.add_parser('use')
    subparser.add_parser('list')

    parser.parse_args()

    args = parser.parse_args()
    command = args.command
    if command == 'use':
        _jvm.use()
    elif command == 'list':
        _jvm.list_paths()
