import os.path
import re
import sys
from handy_tool.util import run_get_output


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} package name')
    # how can I execute and get output?
    pkg = sys.argv[1]
    output = run_get_output(f'pip show {pkg}')
    match = re.search(r"Location:\s*(.*)", output)
    fixed_pkg_name = pkg.replace('-', '_')
    egg_info_path = os.path.join(match.group(1), f'{fixed_pkg_name}.egg-info')
    top_level_path = os.path.join(egg_info_path, 'top_level.txt')
    top_level_content = open(top_level_path).read()
    packages = [line for line in top_level_content.split('\n') if line]
    print(packages)


if __name__ == '__main__':
    main()
