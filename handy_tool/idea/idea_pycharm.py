from .idea_jetbrain import IDeaJetBrains


class IdeaPycharm(IDeaJetBrains):
    def __init__(self):
        super().__init__("pycharm", mac_app_folder_name="PyCharm")


def main():
    IdeaPycharm().main()
