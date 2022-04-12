from .mode.repo_model import Repo
import json
from typing import List
import os
import util.util as util


# for now, use simple []?
def get_repo_list():
    # how do do this?
    content = util.get_file_content(_get_config_path()).strip()
    return [f for f in content.split('\n') if f]


def save_repo_list(repo_list: List[Repo]):
    # how to save?
    config_file_path = _get_config_path()
    util.write_file_content(config_file_path, json.dumps(repo_list))
    

def get_config_file_path():
    # do the snnipt again?
    pass


def _get_config_path():
    return util.expand_config_path("util.python/sync_repo.txt")
