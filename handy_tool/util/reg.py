import subprocess
from typing import List


def fix_path(path):
    path = path.replace('\r\n', '')
    path = path.replace('\n', '')
    return path


def _format_path(path: str) -> str:
    if path.endswith("/"):
        return path[:-1]
    return path


def save_env(key: str, value: str):
    return subprocess.run(
        ['powershell', '-Command', f'[Environment]::SetEnvironmentVariable("{key}", "{value}", "User")'])


def save_path(paths: List[str]):
    return subprocess.run(
        ['powershell', '-Command', f'[Environment]::SetEnvironmentVariable("Path", "{";".join(paths)}", "User")'])


def get_path() -> List[str]:
    output = subprocess.run(['powershell', '-Command', '[Environment]::GetEnvironmentVariable("Path", "User")'],
                            capture_output=True)
    path = output.stdout.decode('utf-8').strip()
    path_list = path.split(";")
    path_list = [_format_path(fix_path(p)) for p in path_list]
    return path_list


def get_path_with_de_duplicate():
    value = get_path()
    return list(dict.fromkeys(value))
