from typing import Optional
import os
from .idea_base import IdeaBase
from ..util.util_find_program import find_program
from ..app import App
from ..util.util_os import is_mac, is_windows

JET_BRAIN_FOLDER_NAME = "JetBrains"


class IDeaJetBrains(IdeaBase):
    def __init__(self, win_folder, win_exe_name='', mac_app_folder_name='', toolbox_bin_name=''):
        """
        Args:
            toolbox_bin_name toolbox可以生成script，比如它会为webstorm生成/usr/local/bin/webstorm，如果是webstorm。传入webstorm
        """
        self.folder_name = win_folder
        self.exe_name = win_exe_name or self.folder_name
        self.mac_app_folder_name = mac_app_folder_name or win_folder
        if is_windows():
            self.jet_brain_folders = find_program(JET_BRAIN_FOLDER_NAME)
        else:
            self.toolbox_bin_name = toolbox_bin_name
            if self.toolbox_bin_name:
                self.toolbox_exe_path = f'/usr/local/bin/{toolbox_bin_name}'
            self.has_toolbox_exe = toolbox_bin_name and os.path.exists(self.toolbox_exe_path)

    def _get_folder(self) -> str:
        for jet_brain_folder in self.jet_brain_folders:
            for fo in os.listdir(jet_brain_folder):
                if self.folder_name in fo.lower():
                    return os.path.join(jet_brain_folder, fo)
        exit('can\'t find folder for order: {}'.format(self.folder_name))

    def _check_user_local_path(self) -> Optional[str]:
        root_path = os.path.expanduser("~/AppData/Local/JetBrains/Toolbox/apps")
        if os.path.exists(root_path):
            sub_folders = os.listdir(root_path)
            for p in sub_folders:
                if self.folder_name.lower() == p.lower():
                    for root, dirs, files in os.walk(os.path.join(root_path, p)):
                        if 'bin' in dirs:
                            # find dir
                            bin_folder = os.path.join(root, 'bin')
                            for f in os.listdir(bin_folder):
                                if f.endswith('.exe') and f.startswith(self.exe_name):
                                    return os.path.join(bin_folder, f)
        return None

    def get_exe_in_win(self) -> str:
        if is_mac():
            return ""
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

    def run(self, args):
        win_path = self.get_exe_in_win()
        mac_exe_path = self.toolbox_exe_path if self.has_toolbox_exe else self.get_exe_in_mac()
        path = win_path if is_windows() else mac_exe_path
        if args.path:
            App(win_path, mac_exe_path).open_file(args.path)
        else:
            print('path is: ', path)