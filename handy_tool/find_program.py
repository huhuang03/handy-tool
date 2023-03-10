import os
import sys

from .util.util_find_program import find_program


def main():
    if not os.name == 'nt':
        exit('only work on window')
    if len(sys.argv) < 2:
        exit(f"usage: {sys.argv[0]} to_find")
    programs = find_program(sys.argv[1])
    if len(programs) == 0:
        print('Can\'t find any program with name {}'.format(sys.argv[1]))
    else:
        print('\n'.join(programs))


if __name__ == '__main__':
    main()
