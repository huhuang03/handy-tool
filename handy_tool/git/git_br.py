from pathlib import Path
import git


def get_last_commit_time(branch):
    return branch.commit.committed_datetime


def list_branch(project_path: Path):
    if not project_path.exists():
        print('why {} not exist'.format(project_path.resolve().__str__()))
        return
    repo = git.Repo(project_path.resolve().__str__())
    branches = repo.branches
    # noinspection PyTypeChecker
    branches = sorted(branches, key=get_last_commit_time)
    # noinspection PyTypeChecker
    for branch in branches:
        last_commit_time = get_last_commit_time(branch)
        print(f'{branch.name} - {last_commit_time}')
