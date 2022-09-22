from encodings import search_function
from genericpath import exists
import os
import shutil
from ...sy import util as _util

def zsh_sync():
    # how to do this?
    _write_sync_file()
    

def _write_sync_file():
    sync_folder = os.path.expanduser(f'~/.sy')
    # write content to it.
    # copy folder to .sy
    if os.path.exists(sync_folder) and os.path.isfile(sync_folder):
        exit("already exit file .sy, I want write to .sy folder!")
    if not os.path.exists(sync_folder):
        os.makedirs(sync_folder)
    src_folder = os.path.join(os.path.dirname(__file__), "asset")
    # do you have better idea to sync folder?
    # why you can't copy?
    shutil.copytree(src_folder, sync_folder, dirs_exist_ok=True)

    # check exits and write if not.
    # with open(sync_bash_path, 'w') as f:
    #     f.write(_CONTENT)
    _util.insert_source_command(os.path.expanduser("~/.zshrc"), "source ~/.sy/.sy.zshrc")
