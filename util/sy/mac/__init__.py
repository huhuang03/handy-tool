from ..comm import git_sync
from .zsh_sync import zsh_sync


def mac_sync():
    git_sync()
    zsh_sync()
