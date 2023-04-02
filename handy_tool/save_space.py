import sys
import os

DST_FOLDER = "~/u/source"

def main():
    """
    This script is for save main dist space.

    In my situation.
    I have all my source code in ~/source/
    And I have a u disk which ln -s at ~/u/
    So my thought is:

    If I have a project at ~/source/xx/yy
    Then I want move it to ~/u/source/xx/yy and link to ~/source/xx/yy
    
    This script is to do this.
    I can run `save_sapce yy` at folder ~/souce/xx. And it do the work for me.

    move from source/xxx to ~/u/source/xxx, and link the dst to src.
    And don't do this when dst exist

    This is only work for me now. Because there are some hardcode path.
    """
    if os.name == 'nt':
        exit('for now we don\'t work on windows')

    global DST_FOLDER
    if len(sys.argv) > 2:
        exit(f"usage: {sys.argv[0]} soruce_folder")

    src_full_path = os.path.abspath(sys.argv[1])
    if not os.path.exists(src_full_path):
        exit(f"{src_full_path} not exit")
    if not os.path.isdir(src_full_path):
        exit(f"{src_full_path} is not a dict")
    
    src_prefix = os.path.expanduser("~/source")
    if not src_full_path.startswith(src_prefix):
        exit(f"we only support handle path begin with {src_prefix}")
    # +1 for /home/xxx/ the end is lost
    src_prefix_len = len(src_prefix)
    if not src_prefix.endswith('/'):
        src_prefix_len += 1
    src_suffix = src_full_path[src_prefix_len:]

    dst_prefix = os.path.expanduser("~/u/source")
    dst_full_path = os.path.join(dst_prefix, src_suffix)

    if os.path.exists(dst_full_path):
        exit(f'{dst_full_path} already exist')
    
    os.system(f'mv {src_full_path} {dst_full_path}')
    os.system(f'ln -s {dst_full_path} {src_full_path}')


if __name__ == "__main__":
    main()