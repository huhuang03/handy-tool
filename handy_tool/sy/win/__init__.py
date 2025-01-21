from ..comm import git_sync
from .powershell import sync_powershell
from .init_wt import _init_windows_terminal


def win_sync():
    git_sync()
    sync_powershell()
    _init_windows_terminal()