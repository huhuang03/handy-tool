import os
from ...sy import util as _util

_CONTENT = """alias jump='export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890'
alias p3=python3
"""

def mac_sync(root: str):
    """
    :param root: the source files root dir
    """
    """How to do the mac sync?"""
    sync_bash_file_name = '.sync_bashrc'
    sync_bash_path = os.path.expanduser(f'~/{sync_bash_file_name}')
    # write content to it.
    with open(sync_bash_path, 'w') as f:
        f.write(_CONTENT)

    path_zshrc = os.path.expanduser('~/.zshrc')
    content_source = f'source ~/{sync_bash_file_name}'
    _util.insert_source_command(path_zshrc, content_source)

def _sync_git_autocomplete():
    # TODO combine this two
    shell = os.environ['SHELL']
    remote_url = ""
    if shell == "/bin/zsh":
        remote_url = "https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.zsh"
    else:
        exit(f"can't handle shell: {shell}")

    file_name = remote_url.split("/")[-1]
    # download to bash.
    # urllib.request.urlretrieve(remote_url, os.path.join(root, file_name))

    source_command = "source ~/.sy/" + file_name