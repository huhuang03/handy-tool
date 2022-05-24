import os
import subprocess
from sys import platform


def run_get_output(cmd):
    output = subprocess.getoutput(cmd)
    return output


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

def confirm(msg):
    """
    Ask user to enter Y or N (case-insensitive).
    :return: True if the answer is Y.
    :rtype: bool
    """
    answer = ""
    while answer not in ["y", "n"]:
        answer = input(f"${msg} [y/N]? ").lower()
        if not answer:
            answer = 'n'
    return answer == "y"