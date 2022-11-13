from ..comm import git_sync
from .init_wt import init_wt
from .powershell import sy_powershell
from .init_wt import sync_windows_terminal


def win_sync():
    git_sync()
    print("init powershell")
    sy_powershell()
    print("init windows terminal")
    sync_windows_terminal()