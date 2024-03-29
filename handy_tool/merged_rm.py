from ast import arg
from pydoc import describe
import subprocess
import argparse

_need_check_branch = ['dev']
_reserve_branch = ["*", "dev", "main", "master", "release"]


def main():
    parser = argparse.ArgumentParser()
    if hasattr(argparse, 'BooleanOptionalAction'):
        parser.add_argument("-c", action=argparse.BooleanOptionalAction, help="compare to current branch")
    else:
        parser.add_argument("-c", action='store_true', help="compare to current branch")

    args = parser.parse_args()

    # print(args)

    output = subprocess.check_output(['git', 'branch', '--merged']).decode('utf-8')
    merged_branches = [item.strip() for item in output.split("\n") if item.strip()]

    for mb in merged_branches:
        if not (mb.startswith('*') or mb in _reserve_branch):
            print(f'delete branch {mb}')
            subprocess.check_output(['git', 'branch', '-d', mb])

        if mb in _need_check_branch:
            print('{} already merged'.format(mb))


if __name__ == '__main__':
    main()
