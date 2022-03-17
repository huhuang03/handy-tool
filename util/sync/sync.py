# Look like that only work in myself situation?
from .emacs_d import sync_emacs_d
from .settings import settings
from .sync_comm import sync_comm


def _sync():
    setting = settings()
    if not setting:
        exit('You must specify a setting.yml file')
    sync_emacs_d()


def main():
    print("ok, begin sync")
    sync_comm()