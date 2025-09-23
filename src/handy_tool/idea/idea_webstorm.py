from .idea_jetbrain import IDeaJetBrains


class IdeaWebstorm(IDeaJetBrains):
    def __init__(self):
        super().__init__("webstorm", toolbox_bin_name='webstorm')


def main():
    IdeaWebstorm().main()