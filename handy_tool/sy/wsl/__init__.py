import os
import shutil

from ..comm import git_sync
from .. import util as _util


def _sync_bash():
    # fist get wsl port
    pass

def wsl_sync():
    git_sync()

    sync_folder = os.path.expanduser(f'~/.sy')
    if os.path.exists(sync_folder) and os.path.isfile(sync_folder):
        exit("already exit file .sy, I want write to .sy folder!")
    if not os.path.exists(sync_folder):
        os.makedirs(sync_folder)
    src_folder = os.path.join(os.path.dirname(__file__), "asset")
    shutil.copytree(src_folder, sync_folder, dirs_exist_ok=True)

    _util.insert_source_command(os.path.expanduser("~/.bashrc"), "source ~/.sy/.sy.zshrc")
