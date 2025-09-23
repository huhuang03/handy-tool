import argparse
import os
from .idea_base import IdeaBase
from ..app import App
import configparser
from ..util import is_windows, is_mac


def _get_android_home(prefer_canary=False):
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
            check_folder = None
            if prefer_canary:
                check_folder = os.path.join(driver_name, "Program Files", "Android", "Android Studio Preview")
            if not check_folder:
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

    def run(self, project_root):
        if not os.path.exists(project_root):
            print(f'project not exists: ${os.path.abspath(project_root)}')
            pass
        mac_path = "/Applications/Android Studio.app"
        if is_mac():
            if self.prefer_canary:
                canary_path = "/Applications/Android Studio Canary.app"
                if os.path.exists(canary_path):
                    mac_path = canary_path
        App(_get_android_home(self.prefer_canary), mac_path).start(project_root)


def main():
    parser = argparse.ArgumentParser(prog='acode', description="quick open with android studio")
    parser.add_argument('-c', '--canary', action='store_true',
                        help='prefer open with canary')
    parser.add_argument('path', nargs="?", default=".")
    args = parser.parse_args()
    IdeaAndroid(args.canary).run(args.path)


if __name__ == '__main__':
    main()
