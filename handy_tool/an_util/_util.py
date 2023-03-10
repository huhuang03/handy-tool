from .. import util
from typing import List


def get_pkgs():
    items = util.run_get_output("adb shell pm list packages -3")
    items: List[str] = items.split("\n")
    pkgs = [item[len('package:'):] for item in items]
    return pkgs
