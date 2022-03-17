from ast import arg
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--push", dest="push", action="store_true", help="run the push")
    parser.add_argument("--no-push", dest="push", action="store_false", help="run the push")
    parser.add_argument("-m", dest="msg", action="store_true", help="quick with msg")
    parser.set_defaults(push=True)
    # msg means popup a msg editor dialog
    parser.set_defaults(msg=False)
    args = parser.parse_args()

    os.system('git add .')

    print(f"args.msg: {args.msg}")
    if args.msg:
        os.system('git commit -a')
    else:
        msg = input('Please input commit message: ')
        if not msg:
            msg = 'update'
        os.system('git commit  -a -m "%s"' % msg)

    if args.push:
        os.system('git push')
