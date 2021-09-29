import subprocess

_need_check_branch = ['dev']
_reserve_branch = ["*", "dev", "main", "master"]


def main():
    output = subprocess.check_output(['git', 'branch', '--merged']).decode('utf-8')
    merged_branches = [item.strip() for item in output.split("\n") if item.strip()]

    for mb in merged_branches:
        if not (mb.startswith('*') or mb in _reserve_branch):
            print(f'delete branch {mb}')
            subprocess.check_output(['git', 'branch', '-d', name])

        if mb in _need_check_branch:
            print('{} already merged'.format(mb))


if __name__ == '__main__':
    main()
