from .idea_jetbrain import IDeaJetBrains
from .base.idea_finder_config import IdeaFinderConfig


class IdeaIntellij(IDeaJetBrains):
    def __init__(self):
        super().__init__("fleet", "fleet", find_config=IdeaFinderConfig(name='Fleet'))


def main():
    IdeaIntellij().main()
