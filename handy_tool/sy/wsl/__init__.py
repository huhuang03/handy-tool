import os
import shutil

from ..comm import git_sync
from .. import util as _util


def _sync_bash():
    # fist get wsl port
    pass


def wsl_sync():
    print('wsl sync begin')
    git_sync()

    target_folder = os.path.expanduser(f'~/.sy')
    if os.path.exists(target_folder) and os.path.isfile(target_folder):
        exit("already exit file .sy, I want write to .sy folder!")
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    src_folder = os.path.join(os.path.dirname(__file__), "asset")
    print(f'src_folder: {src_folder}, target_folder: {target_folder}')
    shutil.copytree(src_folder, target_folder, dirs_exist_ok=True)

    _util.insert_source_command(os.path.expanduser("~/.bashrc"), "source ~/.sy/.sy.bashrc")
