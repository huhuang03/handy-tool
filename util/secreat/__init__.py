# what't the best quick way to do this?
import argparse
import os

MAGIC = b"secreated!!"

def is_on(f_path):
    assert os.path.exists(f_path)
    with open(f_path) as f:
        read_content = f.read(len(MAGIC))
        return read_content == MAGIC


def toggle(f_path):
    if is_on(f_path):
        on(f_path)
    else:
        off(f_path)

def on(f_path: str):
    with open(f_path, 'ra') as f:
        f.write(MAGIC)


def off(f_path: str):
    with open(f_path, 'rw') as f:
        f.seek(len(MAGIC))
        # write to a tmp
        # move back.
        content = f.read()


def main():
    pass
