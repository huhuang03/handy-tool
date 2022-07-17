import os.path


def insert_source_command(file_path: str, source_command: str):
    insert_if_not_exist(file_path, "\n".join(["# added by .sy util\n", source_command]))


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
            print("write content finish")
            f.write(content)
