from . import comm


def repo_list(args):
    repo_list = comm.get_repo_list()
    print('repos: ')
    for repo in repo_list:
        print(repo)
