import os
import sys
import json
# from .sync import _sync
import argparse
from util.util import is_mac, is_windows
import urllib.request
from .mac import mac_sync
from .win import win_sync
from . import repo
from util.util import is_mac, is_windows


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
    if args.command == 'repo':
        args.func(args)
        return

    root_dir = os.path.expanduser("~/.sy")
    if not os.path.exists(root_dir):
        os.makedirs(root_dir, exist_ok=True)

    if is_mac():
        mac_sync(root_dir)

    if is_windows():
        win_sync()