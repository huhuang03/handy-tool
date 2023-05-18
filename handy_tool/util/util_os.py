from sys import platform
from platform import uname


def is_wsl():
    uname_release = uname().release.lower()
    return 'wl' in uname_release and 'microsoft-standard' in uname_release

def is_windows():
    return platform == 'win32'


def is_mac():
    return platform == 'darwin'
