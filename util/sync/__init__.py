import os
import sys
import json
# from .sync import _sync
import argparse
from util.util import is_mac, is_windows
from .mac import mac_sync
from . import repo


def _get_root_path():
    home = os.path.expanduser('~/AppData/Local/Packages')
    # ok, find the home
    for path in os.listdir(home):
        if path.startswith('Microsoft.WindowsTerminal'):
            return os.path.join(home, path)
    return ''


def sync_windows_terminal():
    root = _get_root_path()
    if not root:
        exit('can\'t find window terminal home directory')
    settings_path = os.path.join(root, 'LocalState', 'settings.json')
    data = json.load(open(settings_path))
    print(data)


# how to do this?
def sync_git_autocomplete():
    # how can I do this?
    pass


def main():
    # fk the boring subparsers.
    # print("ok, begin sync")
    parser = argparse.ArgumentParser(description="sync util")
    subparser = parser.add_subparsers(dest="command")
    repo.init_subparser(subparser)
    args = parser.parse_args(sys.argv[1:])
    args.func(args)
    # strange. how can I do this?
    # subparser.add_parser("repo")
    # RepoManager.init_parser(subparser)

    # args = parser.parse_args()
    # if args.command == "repo":
    #     RepoManager(subparser).run(args)
