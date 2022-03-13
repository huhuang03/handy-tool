from ast import arg
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--push", dest="push", action="store_true", help="run the push")
    parser.add_argument("--no-push", dest="push", action="store_false", help="run the push")
    parser.add_argument("-m", dest="msg", action="store_true", help="quick with msg")
    parser.set_defaults(push=True)
    parser.set_defaults(msg=True)
    args = parser.parse_args()

    os.system('git add .')

    if args.msg:
        msg = input('Please input commit message: ')
        if not msg:
            msg = 'update'
        os.system('git commit  -a -m "%s"' % msg)
    else:
        os.system('git commit -a')

    if args.push:
        os.system('git push')
