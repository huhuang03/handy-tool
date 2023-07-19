import os.path
import re
import sys
from handy_tool.util import run_get_output
from typing import List


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} package name')
    # how can I execute and get output?
    pkg = sys.argv[1]
    output = run_get_output(f'pip show {pkg}')
    match = re.search(r"Location:\s*(.*)", output)
    location = match.group(1)
    match = re.search(r"Version:\s*(.*)", output)
    version = match.group(1)
    fixed_pkg_name = pkg.replace('-', '_')

    # test_lib.egg-info
    # opencv_python-4.7.0.72.dist-info
    def find_info_root(extensions: List[str]):
        for name in extensions:
            check_path = os.path.join(location, f'{fixed_pkg_name}{name}')
            if os.path.exists(check_path):
                return check_path

    egg_info_path = find_info_root(['.egg-info', f'-{version}.dist-info'])
    top_level_path = os.path.join(egg_info_path, 'top_level.txt')
    top_level_content = open(top_level_path).read()
    packages = [line for line in top_level_content.split('\n') if line]
    print(packages)


if __name__ == '__main__':
    main()
