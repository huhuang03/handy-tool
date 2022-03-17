# Look like that only work in myself situation?
from .emacs_d import sync_emacs_d
from .settings import settings
import argparse
from .repo import RepoManager


def _sync():
    setting = settings()
    if not setting:
        exit('You must specify a setting.yml file')
    sync_emacs_d()


