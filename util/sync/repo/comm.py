import os
import util.util as util


# for now, use simple []?
def get_repo_list():
    # how do do this?
    content = util.get_file_content(_get_config_path()).strip()
    return [f for f in content.split('\n') if f]


def save_repo_list(path_list):
    path = _get_config_path()
    print(f'path: {path}')
    util.write_file_content(path, "\n".join(path_list))
    

def get_config_file_path():
    # do the snnipt again?
    pass


def _get_config_path():
    return util.expand_config_path("util.python/sync_repo.txt")
