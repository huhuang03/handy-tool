import os
import shutil
from pathlib import Path


def copytree_with_overwrite(src: Path, dst: Path):
    src = src.resolve()
    dst = dst.expanduser().resolve()
    for item in src.rglob('*'):
        print('item: {}'.format(item))
        target = dst / item.relative_to(src)
        print('target: {}'.format(target))
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif item.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
            print('copy from {item} to {target}'.format(item=item, target=target))


def _git_alias_item(alias: str, command: str):
    os.system(f"git config --global alias.{alias} {command}")


def git_sync():
    _git_alias_item("co", "checkout")
    _git_alias_item("ci", "commit")
    _git_alias_item("st", "status")
    _git_alias_item("br", "branch")
    os.system(f"git config --global core.autocrlf false")
    print("config git finish")
