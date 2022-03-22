import os
import util.util as util


# for now, use simple []?
def get_repo_list():
    # how do do this?
    content = util.get_file_content(_get_config_path()).trim()
    return content.split('\n')


def save_repo_list(path_list):
    # how can I do this?
    pass
    

def get_config_file_path():
    # do the snnipt again?
    pass


def _get_config_path():
    return util.expand_config_path("util.python/sync_repo.txt")
