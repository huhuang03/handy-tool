# this will load ide by file type and history
import argparse


def smart_ide():
    parser = argparse.ArgumentParser()
    parser.add_argument('proj_path')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    smart_ide()
