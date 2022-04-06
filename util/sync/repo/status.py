from git import Repo
from . import comm
from util.util import print_red, print_green


def status(args):
    repo_list = comm.get_repo_list()
    first = True
    for repo in repo_list:
        if not first:
            print("")
        print(f"-------- {repo}")
        rst = _check_repo(repo)
        if rst:
            print_green(f"ok")
        first = False


# I want check I have some unpushed commit
# or uncommitted change.
def _check_repo(repo_path):
    """
    :return: false if have some unpushed commit or uncommitted change.
    """
    repo = Repo.init(repo_path)
    if repo.is_dirty():
        print_red("is dirty!!")
        return False

    try:
        check_branch(repo, repo.head.ref)
        check_branch(repo, repo.refs['master'])
    except RuntimeError as err:
        print_red(err.args[0])
    print_green("ok")


def check_branch(repo, local_ref):
    """
    throw msg exction when not up to date.
    """
    tracking_branch = local_ref.tracking_branch()
    if not tracking_branch:
        raise RuntimeError(f"{local_ref} has no remote branch")
    commit_ahead = repo.iter_commits(f"{tracking_branch}..{local_ref}")

    unpushed_commit_count = 0
    if commit_ahead:
        unpushed_commit_count = sum(1 for _ in commit_ahead)

    if unpushed_commit_count > 0:
        raise RuntimeError(f"{local_ref} is ahead {unpushed_commit_count} commits")