from sys import platform
from platform import uname


def is_wsl():
    uname_release = uname().release.lower()
    return 'wsl' in uname_release and 'microsoft-standard' in uname_release


def is_windows():
    return platform == 'win32'


def is_mac():
    return platform == 'darwin'


def is_ubuntu():
    return 'Ubuntu' in uname().version