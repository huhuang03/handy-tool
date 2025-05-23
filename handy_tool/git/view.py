import os
import re
import webbrowser
from typing import Optional
import argparse

from git import Repo, InvalidGitRepositoryError

sub_command = 'view'


def init_sub_command(sub_parser: argparse.ArgumentParser):
    sub_parser.add_argument('path', nargs="?", default=".")
    sub_parser.add_argument('-p', action=argparse.BooleanOptionalAction)
    sub_parser.add_argument('-m', action=argparse.BooleanOptionalAction)


def exec(args):
    view_repo_in_browser(args)


def view_repo_in_browser(args):
    path = args.path
    try:
        path = find_git_root(path)
        repo = Repo(path)
    except InvalidGitRepositoryError:
        print('is not git repo')
        return
    http_url = get_first_http(repo)
    if not http_url:
        print('has no http url')
        return

    if args.p:
        if _is_gitlab(http_url):
            http_url = http_url + '/pulls'
        else:
            http_url = _remove_last_git(http_url) + '/pipelines'
    if args.m:
        if _is_gitlab(http_url):
            http_url = http_url + '/pulls'
        else:
            http_url = _remove_last_git(http_url) + '/merge_requests'
    webbrowser.open(http_url)


def _remove_last_git(str):
    if str.endswith('.git'):
        return str[:-len('.git')]
    return str


def _is_github(url):
    return 'github' in url


def _is_gitlab(path):
    return 'git' in path.split('/')


def get_first_http(repo) -> Optional[str]:
    def _parse(url: str) -> str:
        if url.startswith('http') or url.startswith('https'):
            return url
        if url.startswith('git@github'):
            pattern = re.compile(r'git@github\.com:(.*?)(\.git)?$')
            match = pattern.match(url)
            if match:
                https_url = f'https://github.com/{match.group(1)}'
                return https_url
            else:
                return ''

    for remote in repo.remotes:
        http_url = next(iter([_parse(url) for url in remote.urls]), None)
        if http_url:
            return http_url
    return None


def view_branch_in_browser(branch_name):
    try:
        git_root = find_git_root('.')
        repo = Repo(git_root)
    except InvalidGitRepositoryError:
        print(f'is not git repo')
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


def find_git_root(start_path: str) -> Optional[str]:
    """向上查找直到找到含有 .git 的目录"""
    current = os.path.abspath(start_path)
    while current != os.path.dirname(current):  # 直到到达根目录
        print('current dir:', current)
        if os.path.isdir(os.path.join(current, ".git")):
            return current
        current = os.path.dirname(current)
    return None
