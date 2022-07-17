from sys import platform

def is_windows():
    return platform == 'win32'


def is_mac():
    return platform == 'darwin'
