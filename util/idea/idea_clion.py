from .idea_jebrain import IDeaJetBran


class IdeaPycharm(IDeaJetBran):
    def __init__(self):
        super().__init__("clion")


def main():
    IdeaPycharm().main()
