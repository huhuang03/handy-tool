import argparse
import os.path

from .util.util_os import is_windows
# link all folder in src to dist

def main():
    if not is_windows():
        print("for now, only support windows")
        return
    # check is powershell
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('dst')
    args = parser.parse_args()
    src_full = os.path.abspath(args.src)
    dst_full = os.path.abspath(args.dst)

    if not os.path.exists(src_full) or os.path.isdir(src_full):
        print(f'${src_full} is not exists or is not a folder')
        return

    if not os.path.exists(dst_full) or os.path.isdir(dst_full):
        print(f'${dst_full} is not exists or is not a folder')
        return

    for f in os.listdir(src_full):
        target = os.path.join(dst_full, f)
        if os.path.exists(target):
            print(f'jump {target}')
            continue

        f_full = os.path.join(src_full, f)
        if os.path.islink(f_full):
            print(f'jump {f_full}')
            continue

        # not finish because we need system admin to create linek.
