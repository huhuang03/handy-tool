import subprocess
import os


def insert_front_in_path_temporary(sub_path):
    """
    Not work, because only work in subprocess.
    """
    # I don't know how to do this.
    # subprocess.run(['powershell', '-Command', '$env:aa="cc"'])
    # subprocess.run(['powershell', '-Command', 'Set-Item -Path Env:aa -Value "dd"'])
    # os.system('powershell -Command $env:aa=\"ee\"')
    # os.system('powershell -Command Set-Item -Path Env:aa -Value "ff"')
    pass


def set_in_user(key: str, value: str):
    """set in user scope"""
    command = ['powershell', '-NoProfile', '-Command', f'[Environment]::SetEnvironmentVariable("{key}", "{value}", "User")']
    subprocess.run(command)
