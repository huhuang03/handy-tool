import argparse
import sys


def main():
    if len(sys.argv) <= 1:
        exit("usage: file file_path")

    file_path = sys.argv[1]

    with open(file_path, 'rb') as f:
        first_two_byte = f.read(2)
        print(first_two_byte.hex())