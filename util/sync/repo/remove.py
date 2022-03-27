import os
from . import comm


def remove(args):
    repo_path = os.getcwd()
    repo_list = comm.get_repo_list() or []
    path = os.path.abspath(repo_path)
    if path in repo_list:
        repo_list.remove(path)
    print("remove finish!")
    comm.save_repo_list(repo_list)
