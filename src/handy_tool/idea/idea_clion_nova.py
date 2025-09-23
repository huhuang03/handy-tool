from .idea_jetbrain import IDeaJetBrains


class IdeaClion(IDeaJetBrains):
    def __init__(self):
        super().__init__("Clion-Nova", mac_app_folder_name="CLion Nova", win_exe_name='clion64')


def main():
    IdeaClion().main()
