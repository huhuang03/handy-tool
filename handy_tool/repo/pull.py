import subprocess

from . import comm
from . import cons


def pull(args):
    repo_list = comm.get_repo_list()
    first = True
    print("pull begin")
    print(repo_list)
    for repo in repo_list:
        if not first:
            print("")
        print(f"-------- {repo}")
        repo_dir = repo[cons.KEY_PATH]
        subprocess.Popen(['git', 'pull'], cwd=repo_dir).wait()