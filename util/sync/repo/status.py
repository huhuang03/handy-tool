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
    remote_name = _get_master_track_remote(repo)
    _get_track_remote(repo, "main")
    # what's this?
    commit_ahead = repo.iter_commits(f"{remote_name}/master..master")

    unpushed_commit_count = 0
    if commit_ahead:
        unpushed_commit_count = sum(1 for _ in commit_ahead)

    if unpushed_commit_count > 0:
        print_red(f"Your branch is ahead {unpushed_commit_count} commits")
        return False
    else:
        return True


def _get_master_track_remote(repo):
    """
    get master branch's track remote.
    can you get any other repo?
    """
    # empty_repo.heads.master.set_tracking_branch(origin.refs.master)
    master = repo.heads.master
    remote_master = master.tracking_branch()
    if remote_master is None:
        return "origin"
    return remote_master.remote_name


def _get_track_remote(repo, local_branch_name):
    # TODO: how to get current branch?
    # for repo in repo.heads:
    #     if repo.name == local_branch_name:
    print(repo.heads)
    pass