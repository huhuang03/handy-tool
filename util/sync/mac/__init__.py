import os
import urllib.request
from .. import util as _util


def mac_sync(root: str):
    """
    :param root: the source files root dir
    """
    """How to do the mac sync?"""
    sync_bash_file_name = '.sync_bashrc'
    sync_bash_path = os.path.expanduser(f'~/{sync_bash_file_name}')
    content = 'alias jump=\'export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890\''
    # write content to it.
    with open(sync_bash_path, 'w') as f:
        f.write(content)

    path_zshrc = os.path.expanduser('~/.zshrc')
    # check the .zshrc
    zshrc_content = open(path_zshrc).read()
    content_source = f'source ~/{sync_bash_file_name}'
    if content_source not in zshrc_content:
        zshrc_content = zshrc_content + '\n' + content_source
        with open(path_zshrc, 'w') as f:
            f.write(zshrc_content)

    # TODO combine this two
    shell = os.environ['SHELL']
    remote_url = ""
    if shell == "/bin/zsh":
        remote_url = "https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.zsh"
    else:
        exit(f"can't handle shell: {shell}")

    file_name = remote_url.split("/")[-1]
    # download to bash.
    urllib.request.urlretrieve(remote_url, os.path.join(root, file_name))

    # complete the bash
    source_command = "source ~/.sy/" + file_name

    system_bash_path = os.path.expanduser("~/.zshrc")
    _util.insert_source_command(system_bash_path, source_command)
