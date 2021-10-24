from argparse import ArgumentParser
from .jvm import JVM


def main():
    parser = ArgumentParser()
    subparser = parser.add_subparsers(dest="command")
    subparser.add_parser('clean')
    jvm = JVM()

