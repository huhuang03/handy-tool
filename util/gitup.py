from ast import arg
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--push", dest="push", action="store_true", help="run the push")
    parser.add_argument("--no-push", dest="push", action="store_false", help="run the push")
    parser.set_defaults(push=True)
    args = parser.parse_args()

    os.system('git add .')
    # msg = input('Please input commit message: ')
    # if not msg:
    #     msg = 'update'
    os.system('git commit -a')
    # os.system('git commit --no-verify -a -m "%s"' % msg)
    if args.push:
        os.system('git push')
