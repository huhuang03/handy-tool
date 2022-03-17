import os.path


def expand(sub_folder: str) -> str:
    return os.path.abspath(os.path.expanduser(f"~/.config/{sub_folder}"))
