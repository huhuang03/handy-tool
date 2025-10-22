from argparse import ArgumentParser
from urllib.parse import quote

def main():
    parser = ArgumentParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    print(quote(args.url))
