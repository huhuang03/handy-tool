# this do a clean space
import argparse
import shutil
from pathlib import Path
import glob
import os

def _check_compression_webpack_plugin(path_str):
    path = Path(path_str)
    for item in path.iterdir():
        if item.is_file() and item.name == 'package.json':
            return True
    parent_path = path.parent
    if parent_path == path:
        # means at root
        return False
    return _check_compression_webpack_plugin(parent_path)

def clean_space():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    root_path_str = args.path
    root_path = Path(root_path_str)
    if not root_path.exists():
        print(f'why {root_path} not exists')
        return
    if not root_path.is_dir():
        print(f'why {root_path} is not dir')
        return
    # find folder compression-webpack-plugin and delete
    # need check compression-webpack-plugin in a node package.
    # something is wrong!!
    subfolders = glob.glob(os.path.join(root_path.resolve().__str__(), '**', 'compression-webpack-plugin'), recursive=True)
    for item in subfolders:
        print(f'find item: {item}')
        if _check_compression_webpack_plugin(Path(item)):
            print(f'removing: {item}')
            shutil.rmtree(item)


def main():
    clean_space()

if __name__ == '__main__':
    clean_space()