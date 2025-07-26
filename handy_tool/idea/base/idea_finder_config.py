import dataclasses


@dataclasses.dataclass
class IdeaFinderConfig:
    """
    the name of the idea, like pycharm clion fleet
    """
    name: str


empty_config = IdeaFinderConfig(name='')
