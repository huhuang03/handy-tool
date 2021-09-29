import os
import shutil

_dir = os.getcwd()


def _del(path):
    name = os.path.basename(path)
    if os.path.exists(path):
        print("delete " + name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def command_clean():
    path_cmake_cache = os.path.join(_dir, "CMakeCache.txt")
    _del(path_cmake_cache)
    _del(os.path.join(_dir, "CMakeFiles"))


def clean():
    command_clean()
