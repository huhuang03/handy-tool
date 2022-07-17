# how to do this?
# why you can work?
from util.util.util_os import is_windows
from .win import win_sync


def main():
    if is_windows():
        win_sync()
    else:
        print("only support win now")