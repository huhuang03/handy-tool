import argparse
import os

def _exit():
    exit("TODO: print the help")

def _create(args):
    p_name = args.name
    if not p_name:
        _exit()
    os.system("npx react-native init {} --template react-native-template-typescript".format(p_name))


def main():
    parser = argparse.ArgumentParser(description="rn_ex for now is just for create project")
    subparsers = parser.add_subparsers(help='sub commands', dest="sub_command")
    create = subparsers.add_parser('create', help="create a new project")
    create.add_argument('name', metavar="N", type=str, help="the proejct name")
    args = parser.parse_args()
    if args.sub_command == 'create':
        _create(args)
    else:
        _exit()