import os
import sys
import json
# from .sync import _sync
import argparse
from util.util import is_mac, is_windows
from .mac import mac_sync
from . import repo
import urllib.request


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

    sy_root_dir = os.path.expanduser("~/.sy")
    os.makedirs(sy_root_dir, exist_ok=True)
    shell = os.environ['SHELL']
    remote_url = ""
    if shell == "/bin/zsh":
        remote_url = "https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.zsh"
    else:
        exit(f"can't handle shell: {shell}")

    file_name = remote_url.split("/")[-1]
    # download to bash.
    urllib.request.urlretrieve(remote_url, os.path.join(sy_root_dir, file_name))

    # complete the bash
    source_command = "source ~/.sy/" + file_name

    system_bash_path = os.path.expanduser("~/.zshrc")
    with open(system_bash_path, "r") as f:
        exist = source_command in f.read()

    if not exist:
        with open(system_bash_path, "a") as f:
            f.writelines(["# added by .sy util\n", source_command])
