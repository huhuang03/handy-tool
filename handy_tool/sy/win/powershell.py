import os.path
from .. import util as _util

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


def sy_powershell():
    """@:param root the source files root"""
    profile_path = os.path.expanduser("~\\Documents\\PowerShell\\Microsoft.PowerShell_profile.ps1")

    sy_folder_name = ".sy"
    root = os.path.join(os.path.dirname(profile_path), sy_folder_name)

    sy_file_name = "sy.ps1"
    sy_path = os.path.join(root, sy_file_name)

    if not os.path.exists(root):
        os.makedirs(root)

    with open(sy_path, 'w') as f:
        f.write(_CONTENT)

    source = '. "$PSScriptROOT\\.sy\\sy.ps1"'
    _util.insert_if_not_exist(profile_path, source)