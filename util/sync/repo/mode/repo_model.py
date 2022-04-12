class Repo:
    def __init__(self, path, try_commit) -> None:
        self.path = path
        self.try_commit = try_commit