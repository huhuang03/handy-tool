import os.path
from .. import util as _util
import subprocess

# set-executionpolicy RemoteSigned call this in admin mode
_CONTENT = """
Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete
"""


def win_sync():
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