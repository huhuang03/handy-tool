from .idea_jebrain import IDeaJetBrains


class IdeaPycharm(IDeaJetBrains):
    def __init__(self):
        super().__init__("pycharm", mac_app_folder_name="PyCharm CE")


def main():
    IdeaPycharm().main()