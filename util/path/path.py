from typing import List


class Item:
    def __init__(self, raw: str):
        self.raw = raw
        self.fixed_raw = raw
        if raw.endswith("/"):
            self.fixed_raw = self.fixed_raw[:-1]


class Path:
    items: List[Item] = []

    def __init__(self):
        pass