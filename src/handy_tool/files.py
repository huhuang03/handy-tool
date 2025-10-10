from argparse import ArgumentParser
import magic


def main():
    parser = ArgumentParser()
    parser.add_argument("path", type=str)
    args = parser.parse_args()
    print(magic.from_file(args.path))
