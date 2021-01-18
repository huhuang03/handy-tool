import sys
from pythonex import *
import os
import subprocess
from sys import platform

class JetBrainsApp():
    def __init__(self, win_path, mac_path):
        super().__init__()
        self.win_path = win_path
        self.mac_path = mac_path

    def start(self):
        if len(sys.argv) >= 2:
            dir_name = sys.argv[1]
        else:
            dir_name = "."

        full_dir_path = os.path.abspath(dir_name) 

        if not os.path.exists(full_dir_path):
            raise Exception("Why path not exist: " + full_dir_path)

        if sys.is_win():
            if not os.path.exists(self.win_path):
                raise Exception("Why exe not exist: " + self.win_path)
            # Popen is not good because it will still controled by the proces open the win_path
            # how to start the bat??
            DETACHED_PROCESS = 8
            subprocess.Popen([self.win_path, full_dir_path], cwd=full_dir_path, creationflags=DETACHED_PROCESS, close_fds=True)
        elif sys.is_mac():
            subprocess.Popen(['open', '-a', self.mac_path, dir_name], cwd=full_dir_path)
        else:
            raise Exception(f"Not work on {platform}")
