import os
from .idea_base import IdeaBase
from ..app import App
import configparser
from util.util import is_windows


def _get_android_home():
    if not is_windows():
        return ""
    local_ini_path = os.path.join(os.path.dirname(__file__), "../../local.ini")
    folder = ""
    if os.path.exists(local_ini_path):
        config = configparser.ConfigParser()
        config.read(local_ini_path)
        folder = config['DEFAULT']['AS_HOME']
    else:
        for i in range(ord('A'), ord('Z')):
            driver_name = str(chr(i)) + ":"
            check_folder = os.path.join(driver_name, "Program Files", "Android", "Android Studio")
            if os.path.exists(check_folder):
                folder = check_folder
                break
        else:
            exit("Can't find Android Studio installed folder")
    return os.path.join(folder, "bin", "studio64.exe")


class IdeaAndroid(IdeaBase):
    """
    TODO: If not specify the android home, we need search in all driver
    """
    def run(self, root):
        App(_get_android_home(), "/Applications/Android Studio.app").start()


def main():
    IdeaAndroid().run('')


if __name__ == '__main__':
    main()
