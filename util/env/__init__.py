import subprocess


def set_in_user(key: str, value: str):
    """set in user scope"""
    subprocess.run(['powershell', '-Command', f'[Environment]::SetEnvironmentVariable("{key}", "{value}", "User")'])
