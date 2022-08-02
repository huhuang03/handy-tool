import os
from ssl import HAS_NEVER_CHECK_COMMON_NAME

def init_wt():
    """Init windows terminal"""
    # how about find latest powershell
    start_menu_folder = os.path.join("c:\\", "ProgramData", "Microsoft", 'Windows', "Start Menu", "Programs", "PowerShell")
    has_powershell = os.path.exists(start_menu_folder)
    if not has_powershell:
        print("can't find powershell in start menu")
    else:
        powershell_path = ""
        for f in os.listdir(start_menu_folder):
            if "PowerShell" in f and not "preview" in f:
                powershell_path = os.path.join(start_menu_folder, f)
            
        has_powershell = not not powershell_path

    