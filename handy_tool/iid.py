import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()

    dst_path = Path(parser.path)
    if not dst_path.exists():
        print(f'{dst_path.as_posix()} not exist')
        return

    if dst_path.is_file():
        dst_path = dst_path.parent()

    open_in_file_explorer(path)


def open_in_file_explorer(path: Path):
    system = platform.system()
    if system == "Windows":
        os.startfile(path)
    elif system == "Darwin":  # macOS
        subprocess.run(["open", path])
    else:  # Assume Linux
        subprocess.run(["xdg-open", path])
