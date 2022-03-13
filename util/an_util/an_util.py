import argparse
import os
import time

from .get_apk import get_apk
from .wifi import wifi
from .push_cert import push_cert
from util import util


def _command_push_cert(sub_parser):
    # sub_parser.add_argument("")
    pass


def get_sign(args):
    apk_path = os.path.abspath(args.apk_file)
    if not os.path.exists(apk_path):
        exit(f"apk is not exist {apk_path}")
    os.system(f"keytool -printcert -jarfile {apk_path}")


def screenshot():
    os.system('adb shell screencap -p /sdcard/tmp.jpg')

    file_path = str(round(time.time() * 1000)) + ".jpg"
    os.system(f'adb pull /sdcard/tmp.jpg {file_path}')
    print("Done!")


def main():
    parser = argparse.ArgumentParser(description="android utils")

    subparser = parser.add_subparsers(dest="command")
    parser_push_cert = subparser.add_parser("push_cert", help="push cert file to system cert location(with rename it)")
    parser_push_cert.add_argument("cert_file_path", type=str, help="cert file(like charles cert file)")

    subparser.add_parser("screenshot", help="take a screenshot save name as current time milliseconds.")

    parser_get_sign = subparser.add_parser("get_sign", help="get sign info from apk file")
    parser_get_sign.add_argument("apk_file", type=str, help="print apk sign info")

    parse_get_apk = subparser.add_parser("get_apk", help="get apk by package name")
    parse_get_apk.add_argument("pkg_name", type=str, help="print apk sign info")

    subparser.add_parser("wifi", help="connect adb var wifi")
    subparser.add_parser("ls", help="list all packages.")

    args = parser.parse_args()
    # do you want a map??
    if args.command == "screenshot":
        screenshot()
    elif args.command == "get_sign":
        get_sign(args)
    elif args.command == "get_apk":
        get_apk(args)
    elif args.command == "wifi":
        wifi()
    elif args.command == "push_cert":
        push_cert(args)
    elif args.command == "ls":
        ls()


def ls():
    items = util.run_get_output("adb shell pm list packages -3")
    items: [str] = items.split("\n")
    pkgs = [item[len('package:'):] for item in items]
    print(items)
    pass


if __name__ == "__main__":
    main()