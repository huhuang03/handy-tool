from handy_tool.util.util_os import is_windows, is_mac

alias = [["git", 'g'], "yarn y"]


def main():
    if is_windows():
        from .win import win_sync
        win_sync()
    elif is_mac():
        from .mac import mac_sync
        mac_sync()
    else:
        print("unsupport os")

# def _get_root_path():
#     home = os.path.expanduser('~/AppData/Local/Packages')
#     # ok, find the home
#     for path in os.listdir(home):
#         if path.startswith('Microsoft.WindowsTerminal'):
#             return os.path.join(home, path)
#     return ''


# def sync_windows_terminal():
#     root = _get_root_path()
#     if not root:
#         exit('can\'t find window terminal home directory')
#     settings_path = os.path.join(root, 'LocalState', 'settings.json')
#     data = json.load(open(settings_path))
#     print(data)
