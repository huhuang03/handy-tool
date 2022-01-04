import os


def sync_emacs_d():
    """
    Sync the emacs.d file.
    """
    # ok, first check the we only un committed
    c_folder = os.path.expanduser("~/AppData/Roaming/.emacs.d")
    if os.path.exists(c_folder) and os.path.isdir(c_folder) and not os.path.islink(c_folder):
        # ok, check the git status
        pass
