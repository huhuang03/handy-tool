from importlib.resources import open_binary
import winreg
import subprocess


# reg is reg. nothing else. what can you provide?

def get_value_current_user(sub_key: str, name: str):
    """
    Maybe you confused about the name, but the windows reg is like this. Ok, goon.
    @return the value is (value, type_id), but for now we ignore type_id
    """
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key)
    rst = winreg.QueryValueEx(opened_key, name)
    winreg.CloseKey(opened_key)
    return rst[0]


def set_str_value_current_user(sub_key: str, name: str, value: str):
    """
    很奇怪，需要权限，所以我们下面的方法去设置Enviroment
    """
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key)
    winreg.SetValueEx(opened_key, name, 0, winreg.REG_SZ, value)
    winreg.CloseKey(opened_key)


def set_env_value(env_name: str, env_value: str):
    subprocess.run(
        ['powershell', '-Command', f'[Environment]::SetEnvironmentVariable("{env_name}", "{env_value}", "User")'])
