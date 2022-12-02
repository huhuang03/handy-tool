import argparse
import os
from .idea_base import IdeaBase
from ..app import App
import configparser
from util.util import is_windows, is_mac


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
            driver_name = str(chr(i)) + ":\\"
            check_folder = os.path.join(driver_name, "Program Files", "Android", "Android Studio")
            if os.path.exists(check_folder):
                folder = check_folder
                break
        else:
            exit("Can't find Android Studio installed folder")
    return os.path.join(folder, "bin", "studio64.exe")


class IdeaAndroid(IdeaBase):
    def __init__(self, prefer_canary):
        IdeaBase.__init__(self)
        self.prefer_canary = prefer_canary

    def run(self, root):
        mac_path = "/Applications/Android Studio.app"
        if is_mac():
            if self.prefer_canary:
                canary_path = "/Applications/Android Studio Canary.app"
                if os.path.exists(canary_path):
                    mac_path = canary_path
        App(_get_android_home(), mac_path).start('.')


def main():
    parser = argparse.ArgumentParser(prog='acode', description="quick open with android studio")
    parser.add_argument('-c', '--canary', action='store_true',
                        help='prefer open with canary')
    args = parser.parse_args()
    IdeaAndroid(args.canary).run('')


if __name__ == '__main__':
    main()