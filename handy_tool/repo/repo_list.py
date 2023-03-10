from . import comm
from . import cons


def repo_list(args):
    repos = comm.get_repo_list()
    print('repos: ')
    for repo in repos:
        print(f"path: {repo[cons.KEY_PATH]}, auto_commit: {repo[cons.KEY_AUTO_COMMIT] or False}")
