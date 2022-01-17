import argparse
import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("size")
    args = parser.parse_args()
    size = int(args.size)
    file_name = str(datetime.datetime.now()).replace(':', '_') + '_junk_file.tmp'
    with open(file_name, 'wb') as f:
        index = 0
        while index < size * 1024 * 1024:
            f.write(bytes([0x1]))
            index += 1
    print('done!')
