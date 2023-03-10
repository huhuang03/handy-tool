import os
from git import Repo
import uuid
from .settings import settings
from .. import util

_EMACS_D = '.emacs.d'


def sync_emacs_d():
    """
    Sync the emacs.d file.
    """
    # ok, first check the we only un committed
    c_folder = os.path.expanduser("~/AppData/Roaming/.emacs.d")
    if os.path.exists(c_folder) and os.path.isdir(c_folder) and not os.path.islink(c_folder):
        # ok, check the git status
        repo = Repo(c_folder)
        # can I check has up to date?
        # ok, for now, we only check is_dirty
        if repo.is_dirty():
            exit(f'The origin {c_folder} is not up-to-date, please commit manually.')
        # ok, back up the origin folder
        backup_folder = os.path.join(os.path.dirname(c_folder), f'.emacs.d_back_by_sync_{uuid.uuid4()}')
        print(f'will back up {c_folder} -> {backup_folder}')
        os.rename(c_folder, backup_folder)

    # ok, do the rest.
    setting = settings()
    print(setting['source_dir'])
    # ok, print the
    dist_path = os.path.join(setting['source_dir'], _EMACS_D)
    if not os.path.exists(dist_path):
        Repo.clone_from(url=setting['.emacs_d_repo'], to_path=dist_path)
    # ok, you can go up now!
    util.win.mklink(dist_path, c_folder)