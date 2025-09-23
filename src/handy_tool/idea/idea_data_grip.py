from .idea_jetbrain import IDeaJetBrains


class IdeaDataGrip(IDeaJetBrains):
    def __init__(self):
        super().__init__("DataGrip", "datagrip64")


def main():
    IdeaDataGrip().main()