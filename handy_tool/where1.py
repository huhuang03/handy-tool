import os
import sys


def main():
    if len(sys.argv) < 2:
        print(f'usage {sys.argv[0]} command')
    path_folders = [f for f in os.environ['path'].split(';') if f and os.path.exists(f) and os.path.isdir(f)]
    for item_folder in path_folders:
        for maybe_file in os.listdir(item_folder):
            f_path = os.path.join(item_folder, maybe_file)
            if os.path.isfile(f_path) and maybe_file.startswith(sys.argv[1]):
                print(maybe_file)