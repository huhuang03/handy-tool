from .idea_jetbrain import IDeaJetBrains


class IdeaClion(IDeaJetBrains):
    def __init__(self):
        super().__init__("clion", mac_app_folder_name="CLion Nova")


def main():
    IdeaClion().main()
