from .idea_jetbrain import IDeaJetBrains


class IdeaIntellij(IDeaJetBrains):
    def __init__(self):
        super().__init__("fleet", "fleet")


def main():
    IdeaIntellij().main()