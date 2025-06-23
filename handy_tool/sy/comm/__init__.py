import os


def _git_alias_item(alias: str, command: str):
    os.system(f"git config --global alias.{alias} {command}")


def git_sync():
    _git_alias_item("co", "checkout")
    _git_alias_item("ci", "commit")
    _git_alias_item("st", "status")
    _git_alias_item("br", "branch")
    os.system(f"git config --global core.autocrlf false")
    print("config git finish")
