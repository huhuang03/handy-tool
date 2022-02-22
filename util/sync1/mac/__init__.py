import os


def mac_sync():
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
