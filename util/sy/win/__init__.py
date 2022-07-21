import os.path
from .. import util as _util
from ..comm import git_sync
import subprocess
from util.util.win import mklink

# set-executionpolicy RemoteSigned call this in admin mode
_CONTENT = """
function doJump {
    $Env:http_proxy="http://127.0.0.1:7890";$Env:https_proxy="http://127.0.0.1:7890"
}

function doUnJump {
    Remove-Item Env:http_proxy
    Remove-Item Env:https_proxy
}

New-Alias jump doJump
New-Alias unjump doUnJump
"""


def _back():
    """@:param root the source files root"""
    profile_path = subprocess.run(["powershell", "-c", "echo $profile"], capture_output=True, text=True).stdout.strip()

    sy_folder_name = ".sy"
    root = os.path.join(os.path.dirname(profile_path), sy_folder_name)

    sy_file_name = "sy.ps1"
    sy_path = os.path.join(root, sy_file_name)

    if not os.path.exists(root):
        os.makedirs(root)

    with open(sy_path, 'w') as f:
        f.write(_CONTENT)

    _util.insert_if_not_exist(profile_path, _CONTENT)


def _create_windows_terminal_settings_link(setting_dir: str):
    setting_file = os.path.join(setting_dir, 'settings.json')
    # ok, create symbolic link
    # mklink(os.path.join(os.path.dirname(__file__), 'windows_terminal_config.json'), 'test.json')


def _init_windows_terminal():
    print(os.path.dirname(__file__))
    return
    origin_folder = os.path.expanduser("~/AppData/Local/Packages/")
    for f in os.listdir(origin_folder):
        if f.startswith("Microsoft.WindowsTerminal"):
            origin_folder = os.path.join(origin_folder, f, 'LocalState')
            break
    setting_file = os.path.join(origin_folder, 'settings.json')
    if not os.path.exists(setting_file):
        exit("why can't find windows.terminal settings.json")
    # _create_windows_terminal_settings_link(origin_folder)
    test_file_path = os.path.join(origin_folder, 'test.json')
    print(os.path.exists(test_file_path))
    # can I check this is a real file. not a folder?


def win_sync():
    git_sync()
    _init_windows_terminal()
