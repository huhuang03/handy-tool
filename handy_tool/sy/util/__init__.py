import os.path
from pathlib import Path


def insert_source_command(file_path: str | Path, source_command: str):
    if file_path is Path:
        file_path = file_path.as_posix()
    insert_if_not_exist(file_path, "\n".join(["\n# added by .sy util", source_command]))


def insert_if_not_exist(file_path: str, content: str):
    """
    Insert content in file_path if not exist
    """
    exist = False
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            exist = content in f.read()

    if not exist:
        # 真是奇怪啊。自动加\r 什么意思？
        with open(file_path, "a") as f:
            f.write(content)
