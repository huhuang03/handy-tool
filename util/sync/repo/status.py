import os

from git import Repo
from . import comm
from util.util import print_red, print_green
from . import cons


def status(args):
    repo_list = comm.get_repo_list()
    first = True
    for repo in repo_list:
        if not first:
            print("")
        print(f"-------- {repo}")

        try:
            _check_repo(repo)
        except RuntimeError as err:
            print_red(err.args[0])
        else:
            print_green("ok")
        print("")


# I want check I have some unpushed commit
# or uncommitted change.
def _check_repo(local_repo):
    """
    :return: false if have some unpushed commit or uncommitted change.
    """
    repo_path = local_repo[cons.KEY_PATH]
    auto_commit = local_repo[cons.KEY_AUTO_COMMIT]
    repo = Repo.init(repo_path)

    if repo.is_dirty():
        if auto_commit:
            # try commit
            os.system("git add .")
            os.system('git commit -a -m "auto commit by repo check"')
            os.system('git push')
        else:
            raise RuntimeError("is dirty!!")

    if repo.is_dirty():
        raise RuntimeError("is dirty!!")

    check_branch(repo, repo.head.ref, auto_commit)
    check_branch(repo, repo.refs['master'], auto_commit)


def check_branch(repo, local_ref, auto_commit):
    """
    throw msg exception when not up to date.
    """
    unpushed_commit_count = get_unpushed_commit_count(repo, local_ref)
    if unpushed_commit_count > 0:
        if auto_commit:
            os.system("git push")
        else:
            raise RuntimeError(f"{local_ref} is ahead {unpushed_commit_count} commits")

    unpushed_commit_count = get_unpushed_commit_count(repo, local_ref)
    if unpushed_commit_count > 0:
        raise RuntimeError(f"{local_ref} is ahead {unpushed_commit_count} commits")


def get_unpushed_commit_count(repo, local_ref):
    tracking_branch = local_ref.tracking_branch()
    if not tracking_branch:
        raise RuntimeError(f"{local_ref} has no remote branch")
    commit_ahead = repo.iter_commits(f"{tracking_branch}..{local_ref}")

    unpushed_commit_count = 0
    if commit_ahead:
        unpushed_commit_count = sum(1 for _ in commit_ahead)

    return unpushed_commit_count