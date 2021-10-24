from util import util
import os


class JVM:
    """
    Java version manager

    按照一般软件的开发方式，应该是越来越复杂吧。先做一个简单模型出来
    """
    def __init__(self):
        self._pathes = []
        util.ensure_is_win()
        self._initial()

    def add_pathes(self, path: [str]):
        pass

    def add_one_path(self, path: str):
        self.add_pathes([path])

    def _clean_add_save(self, pathes: [str]):
        pathes = [p for p in pathes if os.path.exists(p)]

    def _initial(self):
        # search in the common path
        if len(self._pathes) == 0:
            print("theres no pathes, so I will do a search.")
            self._init_by_search()

    def _init_by_search(self):
        util.find_folder_by_file_name(
            util.get_folders_in_program_files(["Java"]),
            ["java.exe"]
        )

    def read(self) -> [str]:
        pass

    def _save(self):
        pass