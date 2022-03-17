import os
import json
from .sync import _sync
import argparse
from .repo import RepoManager
from util.util import is_mac, is_windows
from .mac import mac_sync


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


def main():
    # fk the boring subparsers.
    # print("ok, begin sync")
    parser = argparse.ArgumentParser(description="sync util")
    subparser = parser.add_subparsers(dest="command")
    # strange. how can I do this?
    subparser.add_parser("repo")
    RepoManager.init_parser(subparser)

    args = parser.parse_args()
    if args.command == "repo":
        RepoManager(subparser).run(args)
