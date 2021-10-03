from typing import List
import pathlib
import os
_BACKUP_MAX = 10


def add(path):
    """
    add path to backup, because we maybe mess up the path, so we need backup
    :param path:
    :return:
    """
    cache_file_dir = os.path.join(os.path.expanduser('~'), '.util.python/')
    cache_file_path = os.path.join(cache_file_dir, 'path_back.txt')
    pathlib.Path(cache_file_dir).mkdir(exist_ok=True)
    paths: List[str] = []

    if os.path.exists(cache_file_path):
        with open(cache_file_path, 'r') as f:
            paths += [l.strip() for l in f.readlines()]

    if len(paths) > _BACKUP_MAX:
        paths = path[1:]

    paths.insert(0, path)
    with open(cache_file_path, 'w+') as f:
        f.write('\n'.join(paths))

