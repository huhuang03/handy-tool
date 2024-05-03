import os.path
from .. import util as _util

with open(os.path.join(os.path.dirname(__file__), 'asset/sy.ps1')) as f:
    _CONTENT = f.read()


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
