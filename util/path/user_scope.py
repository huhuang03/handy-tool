from typing import List
import os
from .inner.db import add
from ..util import reg


class UserScope:
    def fix_path(self, path):
        path = path.replace('\r\n', '')
        path = path.replace('\n', '')
        return path

    def set_path(self, path: List[str]):
        add(";".join(path))
        return reg.save_path(path)

    def add_cwd_to_path(self):
        old_path_list = reg.get_path_with_de_duplicate()
        if os.getcwd() in old_path_list:
            print("already exist in path")
            return
        rst = self.set_path(old_path_list + [os.getcwd()])
        if not rst.returncode == 0:
            if rst.stderr:
                exit(f"set new_path failed with {rst.stderr.decode('utf-8')}")
            else:
                exit(f"set new_path failed")
    
    def get_path(self) -> List[str]:
        return reg.get_path()


user_scope = UserScope()