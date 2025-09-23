import sys

from .util import *

DETACHED_PROCESS = 8


class App:
    """
    Represent an application
    """
    def __init__(self, win_path='', mac_path='', support_mac=False):
        self.win_path = win_path
        self.mac_app_path = mac_path
        self.support_mac = support_mac or self.mac_app_path

    def open_file(self, file_path):
        full_file_path = os.path.abspath(file_path)

        if not os.path.exists(full_file_path):
            raise Exception("Why path not exist: " + full_file_path)

        folder_path = file_path
        if not os.path.isdir(folder_path):
            folder_path = os.path.dirname(full_file_path)

        if is_windows():
            if not self.win_path:
                exit('exe file not find')
            if not os.path.exists(self.win_path):
                raise Exception("Why exe not exist: " + self.win_path)
            # Popen is not good because it will still controlled by the process open the win_path
            # how to start the bat??
            try:
                subprocess.Popen([self.win_path, full_file_path], cwd=folder_path, creationflags=DETACHED_PROCESS,
                                 close_fds=True)
            except Exception as e:
                print(f"win_path: {self.win_path}")
                raise e
        elif is_mac():
            if not self.support_mac:
                exit('mac not support for now')
            if not self.mac_app_path:
                exit("can't find app path")
            list_command = ['open', '-na', self.mac_app_path, '--args', full_file_path]
            subprocess.Popen(list_command, cwd=folder_path)
        else:
            raise Exception(f"Not work on {platform}")

    def start(self, dir_name=None):
        if not dir_name:
            if len(sys.argv) >= 2:
                dir_name = sys.argv[1]
        if not dir_name:
            dir_name = '.'
        self.open_file(dir_name)