import os
from . import comm


def add(args):
    print("add called!")
    repo_path = os.getcwd()
    repo_list = comm.get_repo_list() or []
    path = os.path.abspath(repo_path)
    if not os.path.exists(path):
        print(f"{path} is exist.")
        return
    if path in repo_list:
        print(f"{path} is already exist")
        return
    repo_list.append(path)
    comm.save_repo_list(repo_list)
