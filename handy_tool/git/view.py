import webbrowser
from typing import Optional

from git import Repo, InvalidGitRepositoryError


def view_repo_in_browser():
    try:
        repo = Repo('.')
    except InvalidGitRepositoryError:
        print('is not git repo')
        return
    http_url = get_first_http(repo)
    if not http_url:
        print('has no http url')
        return
    webbrowser.open(http_url)


def get_first_http(repo) -> Optional[str]:
    try:
        remote = repo.remote()
        http_url = next(iter([url for url in remote.urls if url.startswith('http')]), None)
        if http_url:
            return http_url
    except ValueError:  # remote.remote() will throw this error if no origin remote
        pass
    for remote in repo.remotes:
        http_url = next(iter([url for url in remote.urls if url.startswith('http')]), None)
        if http_url:
            return http_url
    return None


def view_branch_in_browser(branch_name):
    try:
        repo = Repo('.')
    except InvalidGitRepositoryError:
        print('is not git repo')
        return
    for b in repo.branches:
        if b.name == branch_name:
            break
    if not b:
        print(f"can't find branch: {branch_name}")
        return
    http_url = get_first_http(repo)
    if not http_url:
        print("can't find remote http url")
        return
    full_url = f"{http_url}/-/commit/{b.commit}"
    webbrowser.open(full_url)