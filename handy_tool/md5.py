import hashlib
import sys
import os


def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, 'rb') as file:
        # Read the file in chunks to avoid loading large files into memory all at once
        chunk = file.read(4096)
        while chunk:
            sha256_hash.update(chunk)
            chunk = file.read(4096)

    return sha256_hash.hexdigest()


def main():
    if len(sys.argv) < 2:
        print(f'usage: {sys.argv[0]} path')
    path = sys.argv[1]
    print(calculate_file_hash(path))
