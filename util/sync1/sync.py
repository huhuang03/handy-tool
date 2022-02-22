# Look like that only work in myself situation?
from .emacs_d import sync_emacs_d
from .settings import settings


def _sync():
    setting = settings()
    if not setting:
        exit('You must specify a setting.yml file')
    sync_emacs_d()


def main():
    print('should not be here')