import os
import subprocess
from pathlib import Path

_sizes = []

def _output():
    print('\r', end='')
    for size in _sizes:
        print(size)

def main():
    command = ['du', '-d', '0']
    for f in os.listdir('.'):
        command.append(f)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
    for line in p.stdout:
        if line != '':
            line = line.strip()
            _sizes.append(line)
        _output()


if __name__ == '__main__':
    main()