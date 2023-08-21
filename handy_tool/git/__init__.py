import argparse
import webbrowser
from typing import Optional

from git import Repo, InvalidGitRepositoryError


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


def main():
    parser = argparse.ArgumentParser(description="git util")
    subparsers = parser.add_subparsers(dest='sub_command')

    subparsers.add_parser('view', help='view repo in browser')

    args = parser.parse_args()
    if args.sub_command == 'view':
        view_repo_in_browser()
