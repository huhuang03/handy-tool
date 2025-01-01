from .idea_jetbrain import IDeaJetBrains


class IdeaRustRover(IDeaJetBrains):
    def __init__(self):
        super().__init__("RustRover", "rustrover64")


def main():
    IdeaRustRover().main()
