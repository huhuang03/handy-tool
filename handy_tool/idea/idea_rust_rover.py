from .idea_jetbrain import IDeaJetBrains


class IdeaRustRover(IDeaJetBrains):
    def __init__(self):
        super().__init__("RustRover", mac_app_folder_name="RustRover")


def main():
    IdeaRustRover().main()
