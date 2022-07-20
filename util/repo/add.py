import os
from . import comm
from . import cons


def add(args):
    repo_path = os.getcwd()
    repo = {cons.KEY_PATH: repo_path, cons.KEY_AUTO_COMMIT: args.auto_commit or False}
    repo_list = comm.get_repo_list() or []
    path = os.path.abspath(repo_path)
    if not os.path.exists(path):
        print(f"{path} is exist.")
        return

    for item in repo_list:
        if item[cons.KEY_PATH] == path:
            repo_list.remove(item)

    repo_list.append(repo)
    comm.save_repo_list(repo_list)
