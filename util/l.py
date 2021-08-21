import os
from .util.util import ensure_is_win
import subprocess


def main():
    ensure_is_win()
    subprocess.run(['powershell', '-Command', f'Get-ChildItem |Sort-Object LastWriteTime'])

main()