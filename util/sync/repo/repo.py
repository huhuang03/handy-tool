import os
import subprocess
from util import config
import yaml

repo_path_list = []


# I don't want use something like global, so I use class. fuck
# How do you think about the setting format?
# separate of combine?
#

class RepoManager:
    def __init__(self, subparser):
        self.repo_path_list = self.load()
        self._config_path = RepoManager._config_file_path()
        print(self._config_path)

    @staticmethod
    def init_parser(subparser):
        subparser.add_subparsers(dest="command")
        pass

    def run(self, arg):
        # fk, I don't want to add subcommand again.
        pass

    def load(self) -> [str]:
        # yaml.dump(self.)
        return []

    def save(self):
        if not self.repo_path_list:
            return
        yaml_data = yaml.dump(self.repo_path_list)
        print(yaml_data)

    def add(self):
        path = os.getcwd()
        if path not in self.repo_path_list:
            self.repo_path_list.append(path)
        self.save()

    def state(self):
        for repo in self.repo_path_list:
            if not os.path.exists(repo):
                print("jump directory " + repo + " because not exist")
                continue

            subprocess.call("git status", cwd=repo)
        print("done")

    @staticmethod
    def _config_file_path() -> str:
        return config.expand("util.python/sync_repo.yml")
