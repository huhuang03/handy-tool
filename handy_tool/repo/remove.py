import os
from . import comm


def remove(args):
    repo_path = os.getcwd()
    if args.path:
        repo_path = args.path
    repo_list = comm.get_repo_list() or []
    path = os.path.abspath(repo_path)
    for repo in repo_list:
        if repo['path'] == path:
            repo_list.remove(repo)
            break
    print("remove finish!")
    comm.save_repo_list(repo_list)
