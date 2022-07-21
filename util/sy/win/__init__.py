import os.path
from .. import util as _util
from ..comm import git_sync
import subprocess

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


def win_sync():
    git_sync()
