import winreg

REG_KEY_CURRENT_VERSION = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion"

REG_SUB_KEY_PROGRAM_FILE_DIR = "ProgramFielsDir"
REG_SUB_KEY_PROGRAM_FILE_DIR_X86 = "ProgramFielsDir(x86)"


def set_default_install_path():
    """
    First show the current.
    """
    print(winreg.QueryValue(REG_KEY_CURRENT_VERSION, REG_SUB_KEY_PROGRAM_FILE_DIR))


def setup_win():
    set_default_install_path()