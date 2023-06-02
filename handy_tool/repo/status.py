from argparse import ArgumentParser
import os
import subprocess

from git import Repo
from . import comm
from handy_tool.util import print_red, print_green
from . import cons


def status(args):
    list_mode = args.list
    repo_list = comm.get_repo_list()
    rst = []
    for repo in repo_list:
        print(f'checking: {repo["path"]}', end='\r')
        try:
            _check_repo(repo)
        except RuntimeError as err:
            rst.append({'repo': repo, 'error': err.args[0]})
        else:
            rst.append({'repo': repo})

    if list_mode:
        first = True
        for item in rst:
            if not first:
                print("")
            print(f"-------- {item['repo']}")
            if item['error']:
                print_red(item['error'])
            else:
                print_green("ok")
        print("")
    else:
        syned_repos = [item for item in rst if 'error' not in item]
        error_repos = [item for item in rst if 'error' in item]
        print('syned repos: ')
        if len(syned_repos) == 0:
            print('\tAll repo syned')
        else:
            for item in syned_repos:
                print(item['repo'])

        print('\nnot syned repos:')
        if len(error_repos) == 0:
            print('\t All repo syned')
        else:
            for item in error_repos:
                print_red(f"{item['repo']}")


def init_parser(parser: ArgumentParser):
    parser.set_defaults(func=status)
    parser.add_argument('-l', '--list', action='store_true')


# I want check I have some unpushed commit
# or uncommitted change.
def _check_repo(local_repo):
    """
    :return: false if have some unpushed commit or uncommitted change.
    """
    repo_path = local_repo[cons.KEY_PATH]
    auto_commit = local_repo[cons.KEY_AUTO_COMMIT]
    if not os.path.exists(repo_path):
        print(f"{repo_path} not exists")
        return
    repo = Repo.init(repo_path)
    repo_dir = repo_path

    if repo.is_dirty() or _has_uncommit(repo):
        if auto_commit:
            # try commit
            # TODO check that diff files total size is < 5M, to avoid wrong upload big file.
            subprocess.Popen(['git', 'add', '.'], cwd=repo_dir).wait()
            subprocess.Popen(['git', 'commit', '-a', '-m', '"auto commit by repo check"'], cwd=repo_dir).wait()
            subprocess.Popen(['git', 'push'], cwd=repo_dir).wait()
        else:
            _check_dirty_or_uncommit_with_throw(repo)

    _check_dirty_or_uncommit_with_throw(repo)

    check_branch(repo, repo.head.ref, auto_commit)
    if 'master' in repo.refs:
        check_branch(repo, repo.refs['master'], auto_commit)


def _check_dirty_or_uncommit_with_throw(repo):
    if repo.is_dirty():
        raise RuntimeError("is dirty!!")

    if _has_uncommit(repo):
        raise RuntimeError("has un-commit files")


def _has_uncommit(repo):
    return len(repo.untracked_files) > 0


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
