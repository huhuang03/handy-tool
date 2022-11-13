import os

def sync_windows_terminal():
    pass


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


def init_wt():
    """Init windows terminal"""
    # how about find latest powershell
    start_menu_folder = os.path.join("c:\\", "ProgramData", "Microsoft", 'Windows', "Start Menu", "Programs",
                                     "PowerShell")
    has_powershell = os.path.exists(start_menu_folder)
    if not has_powershell:
        print("can't find powershell in start menu")
    else:
        powershell_path = ""
        for f in os.listdir(start_menu_folder):
            if "PowerShell" in f and not "preview" in f:
                powershell_path = os.path.join(start_menu_folder, f)

        has_powershell = not not powershell_path

def _create_windows_terminal_settings_link(setting_dir: str):
    setting_file = os.path.join(setting_dir, 'settings.json')
    # ok, create symbolic link
    # mklink(os.path.join(os.path.dirname(__file__), 'windows_terminal_config.json'), 'test.json')
