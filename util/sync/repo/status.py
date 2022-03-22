from . import comm
import subprocess


def status(args):
    repo_list = comm.get_repo_list()
    for repo in repo_list:
        print(f"------in {repo}")
        subprocess.run("git status", cwd=repo)
