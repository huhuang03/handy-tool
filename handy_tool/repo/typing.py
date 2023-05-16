from typing import TypedDict


class Repo(TypedDict):
    auto_commit: bool
    path: str