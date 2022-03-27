from git import Repo
from . import comm
import subprocess


def status(args):
    repo_list = comm.get_repo_list()
    first = True
    for repo in repo_list:
        if not first:
            print("")
        print(f"-------- {repo}")
        subprocess.run("git status", shell=True, cwd=repo)
        _check_repo(repo)
        first = False


# I want check I have some unpushed commit
# or uncommitted change.
def _check_repo(repo_path):
    """
    :return: false if have some unpushed commit or uncommitted change.
    """
    repo = Repo.init(repo_path)
    if repo.is_dirty():
        print("is dirty!!!!!")
        return False
    if repo.head.ref != repo.refs['origin/master']:
        print("look have some thing not commit!")
    return True