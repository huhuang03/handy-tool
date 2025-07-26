import argparse
from typing import Optional
from pathlib import Path
import os
from .idea_base import IdeaBase
from ..util.util_find_program import find_program
from ..app import App
from ..util.util_os import is_mac, is_windows
from .base.idea_finder_config import IdeaFinderConfig, empty_config

JET_BRAIN_FOLDER_NAME = "JetBrains"


def walk_reverse(root):
    """
    :return: like os.walk, but order folder desc, because  we want find bigger versin first.
    """
    if not os.path.exists(root):
        raise FileNotFoundError(root)
    if os.path.isfile(root):
        return
    all_files_and_folder = os.listdir(root)
    all_files = [f for f in all_files_and_folder if os.path.isfile(os.path.join(root, f))]
    all_folders = [f for f in all_files_and_folder if os.path.isdir(os.path.join(root, f))]
    yield root, list(reversed(all_folders)), all_files
    for folder in reversed(all_folders):
        yield from walk_reverse(os.path.join(root, folder))


class IDeaJetBrains(IdeaBase):
    def __init__(self,
                 win_folder,
                 win_exe_name='', mac_app_folder_name='', toolbox_bin_name='',
                 find_config: IdeaFinderConfig = empty_config):
        """
        Args:
            toolbox_bin_name toolbox可以生成script，比如它会为webstorm生成/usr/local/bin/webstorm，如果是webstorm。传入webstorm
        """
        self.has_toolbox_exe = False
        self.folder_name = win_folder
        self.find_config = find_config
        self.exe_name = win_exe_name or self.folder_name
        self.mac_app_folder_name = mac_app_folder_name or win_folder
        if is_windows():
            self.jet_brain_folders = find_program(JET_BRAIN_FOLDER_NAME)
            toolbox_app_folder = Path('~/AppData/Local/JetBrains/Toolbox/apps').expanduser()
            # why has multy?
            if os.path.exists(toolbox_app_folder):
                self.jet_brain_folders.append(toolbox_app_folder.resolve().__str__())
            if os.path.exists(os.path.expanduser('~/AppData/Local/Programs')):
                self.jet_brain_folders.append(os.path.expanduser('~/AppData/Local/Programs'))
        else:
            self.toolbox_bin_name = toolbox_bin_name
            if self.toolbox_bin_name:
                self.toolbox_exe_path = f'/usr/local/bin/{toolbox_bin_name}'
            self.has_toolbox_exe = toolbox_bin_name and os.path.exists(self.toolbox_exe_path)

    def _get_folder(self) -> str:
        """
        :return:
        """
        for jet_brain_folder in self.jet_brain_folders:
            for fo in os.listdir(jet_brain_folder):
                if self.folder_name.lower() in fo.lower():
                    return os.path.join(jet_brain_folder, fo)
        # 现在已经是直接安装了
        find_in_programs = find_program(self.folder_name)
        if find_in_programs:
            return find_in_programs[0]
        exit('can\'t find folder for order: {} in folders: {}'.format(self.folder_name, self.jet_brain_folders))

    def _check_user_local_path(self) -> Optional[str]:
        root_path = os.path.expanduser("~/AppData/Local/JetBrains/Toolbox/apps")
        # 按照version倒序比较好
        if os.path.exists(root_path):
            sub_folders = os.listdir(root_path)
            for p in sub_folders:
                if self.folder_name.lower() == p.lower():
                    # 这里我想倒叙
                    for root, dirs, files in walk_reverse(os.path.join(root_path, p)):
                        if 'bin' in dirs:
                            # find dir
                            bin_folder = os.path.join(root, 'bin')
                            for f in os.listdir(bin_folder):
                                if f.endswith('.exe') and f.startswith(self.exe_name):
                                    return os.path.join(bin_folder, f)
        return None

    def _find_path_in_toolbox(self) -> Optional[Path]:
        """
        for now only check in windows
        has
        """
        if not self.find_config.name:
            return None
        toolbox_app_root = _get_toolbox_app_folder()
        if not toolbox_app_root:
            return None
        return _get_ch_path(toolbox_app_root / self.find_config.name)

    def _get_exe_in_win(self) -> str:
        """
        find the exe path in win
        :return:
        """
        if is_mac():
            return ""
        path_in_toolbox = self._find_path_in_toolbox()
        if path_in_toolbox:
            return path_in_toolbox.as_posix()

        user_local_path = self._check_user_local_path()
        if user_local_path:
            return user_local_path
        app_folder = self._get_folder()
        bin_folder = os.path.join(app_folder, 'bin')

        bin_file = ""
        for fo in os.listdir(bin_folder):
            if fo.endswith('.exe') and self.exe_name in fo:
                bin_file = fo
        bin_path = os.path.join(bin_folder, bin_file)
        return bin_path

    def get_exe_in_mac(self) -> str:
        if is_windows():
            return ""
        if not self.mac_app_folder_name:
            return ""
        apps_folder = "/Applications"

        def find_folder(root):
            for i in os.listdir(root):
                if self.mac_app_folder_name.lower() in i.lower() and i.endswith(".app"):
                    return os.path.join(root, i)

        found = find_folder(apps_folder)
        if found:
            return found

        tool_box_path = os.path.expanduser("~/Applications/JetBrains Toolbox")
        found = find_folder(tool_box_path)
        if found:
            return found
        return ""

    def _setup_parser(self, parser: argparse.ArgumentParser):
        parser.add_argument('-c', help='prepare use community edition', action=argparse.BooleanOptionalAction)

    def run(self, args):
        win_path = self._get_exe_in_win()
        mac_exe_path = self.toolbox_exe_path if self.has_toolbox_exe else self.get_exe_in_mac()
        path = win_path if is_windows() else mac_exe_path
        if args.path:
            App(win_path, mac_exe_path).open_file(args.path)
        else:
            print('path is: ', path)


def _get_ch_path(app_path: Path) -> Optional[Path]:
    """
    toolbox/apps/xxxx(Fleet)/ch-0/.shellLnk, the content
    @:param app_path: like toolbox/apps/xxxx(Fleet)
    :return:
    """
    shell_link_path = app_path / 'ch-0/.shellLink'
    print('shell_link_path: {}'.format(shell_link_path))
    if not shell_link_path.exists():
        return None
    text = shell_link_path.read_text()
    link_path = Path(text)
    return link_path if link_path.exists() else None


def _get_toolbox_app_folder() -> Optional[Path]:
    """
    get the toolbox app folder, none if not found
    :return:
    """
    p = Path('~/AppData/Local/JetBrains/Toolbox/apps').expanduser()
    return p if p.exists() else None
