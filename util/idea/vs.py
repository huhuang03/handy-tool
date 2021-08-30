import os
from .idea_base import IdeaBase
from ..util.util_find_program import find_file
from ..app import App

SUFFIX = ".sln"


class IdeaVs(IdeaBase):
    def get_sln_path(self, file_path: str):
        if file_path.endswith(SUFFIX):
            return file_path
        if os.path.isdir(file_path):
            sln_path = next((p for p in os.listdir(file_path) if p.endswith(SUFFIX)), '')
            if sln_path:
                return sln_path
        return ''

    def get_vs_exe_path(self):
        return find_file(['Microsoft Visual Studio', '2019', 'Professional', 'Common7', 'IDE'])

    def run(self, file_path):
        sln_file_path = self.get_sln_path(file_path)
        if not sln_file_path:
            exit('Cannot find the sln file, please check')
        vs_exe_path = self.get_vs_exe_path()
        print(f'vs_exe_path {vs_exe_path}')
        App(vs_exe_path, sln_file_path).open_file(sln_file_path)


def main():
    IdeaVs().main()