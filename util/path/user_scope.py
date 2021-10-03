from typing import List
import os
import subprocess
from .inner.db import add


class UserScope:
    def fix_path(self, path):
        path = path.replace('\r\n', '')
        path = path.replace('\n', '')
        return path

    def _set_path(self, path: str):
        add(path)
        rst = subprocess.run(['powershell', '-Command', f'[Environment]::SetEnvironmentVariable("Path", "{path}", "User")'])
        return rst

    def set_path(self, path: List[str]):
        return self._set_path(";".join(path))

    def get_path(self) -> [List[str], str]:
        output = subprocess.run(['powershell', '-Command', '[Environment]::GetEnvironmentVariable("Path", "User")'], capture_output=True)
        path = output.stdout.decode('utf-8').strip()
        path = self.fix_path(path)
        path_list = path.split(";")
        return path_list, path

    def add_cwd_to_path(self):
        old_path_list, old_path = self.get_path()
        if os.getcwd() in old_path_list:
            print("already exist in path")
            return
        new_path = old_path + ";" + os.getcwd()
        rst = self.set_path(new_path.split(";"))
        if not rst.returncode == 0:
            if rst.stderr:
                exit(f"set new_path failed with {rst.stderr.decode('utf-8')}")
            else:
                exit(f"set new_path failed")


user_scope = UserScope()