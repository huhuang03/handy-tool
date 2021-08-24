import os
from sys import platform


def ensure_is_win():
    if not is_windows():
        exit('only work on windows')


def add_to_clip_board(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


def is_windows():
    return platform == 'win32'


def is_mac():
    return platform == 'darwin'