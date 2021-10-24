from argparse import ArgumentParser
from .jvm import JVM


def main():
    _jvm = JVM()
    parser = ArgumentParser()
    subparser = parser.add_subparsers(dest="command")
    subparser.add_parser('use')

    parser.parse_args()

    args = parser.parse_args()
    command = args.command
    if command == 'use':
        _jvm.use()
