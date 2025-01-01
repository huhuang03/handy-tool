import sys
import os
from pathlib import Path
import argparse

DEFUALT_SRC_FOLDER = Path("~/source1").expanduser().resolve().__str__()

DEFUALT_DST_FOLDER = Path("~/source").expanduser().resolve().__str__()

def main():
    """
    This script is for save main dist space.

    In my situation.
    I have all my source folder in ~/source/
    and my u dist source folder in ~/source1/

    And I want soft link all (fodler or file)(level 0) in source1 to source. So I can just ignore where the source project
    is and just look in soruce.
    """
    if os.name == 'nt':
        exit('for now we don\'t work on windows')

    parser = argparse.ArgumentParser(description='link all file in src fodler to dst folder')
    parser.add_argument("-s", "--source_folder", default=DEFUALT_SRC_FOLDER,)
    parser.add_argument("-d", "--dst_folder", default=DEFUALT_DST_FOLDER,)
    args = parser.parse_args()
    source_folder = Path(args.source_folder)
    dst_folder = Path(args.dst_folder)
    if not source_folder.exists():
        exit(f'source_folder {source_folder} does not exist')
    if not dst_folder.exists():
        exit(f'dst_folder {dst_folder} does not exist')

    if not source_folder.is_dir():
        exit(f'source_folder {source_folder} is not a directory')
    if not dst_folder.is_dir():
        exit(f'dst_folder {dst_folder} is not a directory')

    for file in source_folder.iterdir():
        if not file.is_dir():
            continue
        name = file.name
        in_dst = dst_folder / name
        if in_dst.exists():
            print(f'{in_dst} already exists')
            continue
        in_dst.symlink_to(source_folder / name, target_is_directory=True)

if __name__ == "__main__":
    main()