from .idea_jetbrain import IDeaJetBrains


class IdeaClion(IDeaJetBrains):
    def __init__(self):
        super().__init__(win_folder="goland", mac_app_folder_name="GoLand")


def main():
    IdeaClion().main()
