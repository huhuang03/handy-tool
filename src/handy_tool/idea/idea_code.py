from .idea_base import IdeaBase
import subprocess


class IdeaCode(IdeaBase):
    def run(self, root):
        subprocess.run(['code', root])