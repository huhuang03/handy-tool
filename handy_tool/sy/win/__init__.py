from ..comm import git_sync
from .powershell import sy_powershell
from .init_wt import _init_windows_terminal


def win_sync():
    git_sync()
    print("init powershell")
    sy_powershell()
    print("init windows terminal")
    _init_windows_terminal()