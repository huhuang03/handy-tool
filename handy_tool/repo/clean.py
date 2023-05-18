import os.path

from handy_tool.util import confirm
from . import comm
from .comm import save_repo_list


def clean(args):
    """
    return all not exists repo
    """
    repos = comm.get_repo_list()
    to_remove = []
    for repo in repos:
        p = repo['path']
        if not os.path.exists(p):
            to_remove.append(repo)

    if len(to_remove) == 0:
        print("already clean")
    else:
        msg = '\n'.join([f'{index} {item["path"]}' for index, item in enumerate(to_remove)])
        ok = confirm(f"will remove: \n{msg}\nConfirm:")
        if ok:
            removed = [p for p in repos if len([f for f in to_remove if f['path'] == p['path']]) == 0]
            save_repo_list(removed)
