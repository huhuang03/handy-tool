from . import comm
import subprocess


def status(args):
    repo_list = comm.get_repo_list()
    first = True
    for repo in repo_list:
        if not first:
            print("")
        print(f"------in {repo}")
        subprocess.run("git status", shell=True, cwd=repo)
        first = False
