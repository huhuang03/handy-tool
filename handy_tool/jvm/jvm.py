from handy_tool import util
import inquirer
import os
from .. import env


class JVM:
    """
    Java version manager

    按照一般软件的开发方式，应该是越来越复杂吧。先做一个简单模型出来
    """
    def __init__(self):
        self._paths = []
        util.ensure_is_win()
        self._initial()

    def list_paths(self):
        for path in self._paths:
            print(path)

    def add_paths(self, path: [str]):
        pass

    def add_one_path(self, path: str):
        self.add_paths([path])

    def _clean_add_save(self, paths: [str]):
        paths = [p for p in paths if os.path.exists(p)]

    def _initial(self):
        # search in the common path
        if len(self._paths) == 0:
            # print("theres no pathes, so I will do a search.")
            bin_paths = self._init_by_search()
            self._paths = [os.path.dirname(f) for f in bin_paths]

    def _init_by_search(self) -> [str]:
        return util.find_folder_by_file_name(
            util.get_folders_in_program_files(["Java"]),
            ["java.exe"]
        )

    def use(self):
        choice = inquirer.prompt([
            inquirer.List('path',
                          message='Which path you want use',
                          choices=self._paths)
        ])
        print(f"choice: {choice}, java_home: {choice['path']}")
        if choice:
            env.insert_front_in_path_temporary("")
            env.set_in_user('JAVA_HOME', choice['path'])
            # but how to let the path active immediately
            print('done')
        else:
            print("not choice")

    def read(self) -> [str]:
        pass

    def _save(self):
        pass