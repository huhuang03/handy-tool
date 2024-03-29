from .comm import git_sync
from handy_tool.util.util_os import is_windows, is_mac, is_wsl

alias = [["git", 'g'], "yarn y"]


def main():
    if is_windows():
        from .win import win_sync
        win_sync()
    elif is_mac():
        from .mac import mac_sync
        mac_sync()
    elif is_wsl():
        from .wsl import wsl_sync
        wsl_sync()
    else:
        git_sync()