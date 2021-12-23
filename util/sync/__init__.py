import os
import pyjson5 as json


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
    sync_windows_terminal()