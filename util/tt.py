import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()
    print(subparser)
    # can it be optional?
    sub1_parser = subparser.add_parser("sub1", help="sub1 help")

    sub1_subparsers = sub1_parser.add_subparsers()
    sub11_parser = sub1_subparsers.add_parser("sub11")
    print(sub11_parser)
    sub11_parser.add_argument("-foo", help="foo in sub11")

    sub2_parser = subparser.add_parser("sub2", help="sub2 help")

    sub3_parser = subparser.add_parser("sub3", help="sub3 help")

    parser.parse_args(sys.argv[1:])
    
