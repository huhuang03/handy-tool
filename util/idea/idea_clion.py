from .idea_jetbrain import IDeaJetBrains


class IdeaClion(IDeaJetBrains):
    def __init__(self):
        super().__init__("clion")


def main():
    IdeaClion().main()
