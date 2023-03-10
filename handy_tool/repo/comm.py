import json

import yaml

import handy_tool.util as util

_REPO_KEY = "repos"


# for now, use simple []?
def get_repo_list():
    # how do this?
    content = util.get_file_content(_get_config_path()).strip()
    loaded = yaml.safe_load(content)
    if not loaded:
        return []
    if _REPO_KEY in loaded:
        return loaded[_REPO_KEY]
    else:
        return []


def save_repo_list(repo_list):
    repo_str = yaml.dump({_REPO_KEY: repo_list})
    # how to save?
    config_file_path = _get_config_path()
    util.write_file_content(config_file_path, repo_str)
    

def _get_config_path():
    return util.expand_config_path("util.python/sync_repo.yaml")
