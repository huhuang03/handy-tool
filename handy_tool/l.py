import subprocess

from .util.util import ensure_is_win


def main():
    ensure_is_win()
    subprocess.run(['powershell', '-Command', f'Get-ChildItem |Sort-Object LastWriteTime'])