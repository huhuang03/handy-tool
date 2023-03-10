from .idea_jetbrain import IDeaJetBrains


class IdeaIntellij(IDeaJetBrains):
    def __init__(self):
        super().__init__("intellij", "idea64")


def main():
    IdeaIntellij().main()