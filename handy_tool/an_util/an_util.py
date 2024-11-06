import argparse
import os
import subprocess
import tempfile
import time
import re

from .get_apk import get_apk
from .wifi import wifi
from .push_cert import push_cert
from handy_tool import util
from . import get_apk


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


MD5_COMMAND_PATH = "path"
MD5_COMMAND_PWD = "pwd"
MD5_COMMAND_ALIAS = "alias"

def main():
    parser = argparse.ArgumentParser(description="android utils")

    subparser = parser.add_subparsers(dest="command")
    parser_push_cert = subparser.add_parser("push_cert", help="push cert file to system cert location(with rename it)")
    parser_push_cert.add_argument("cert_file_path", type=str, help="cert file(like charles cert file)")

    get_apk.init_args(subparser)

    subparser.add_parser("screenshot", help="take a screenshot save name as current time milliseconds.")

    parser_get_sign = subparser.add_parser("get_sign", help="get sign info from apk file")
    parser_get_sign.add_argument("apk_file", type=str, help="print apk sign info")

    subparser.add_parser("wifi", help="connect adb var wifi")
    subparser.add_parser("ls", help="list all packages.")

    parser_sign_info = subparser.add_parser("sign_info", help="get sign info from sign file")
    parser_sign_info.add_argument("path", help="sign file path")
    parser_sign_info.add_argument("pwd", help="pwd")
    parser_sign_info.add_argument("alias", help="the alias")

    args = parser.parse_args()
    # do you want a map??
    if args.command == "screenshot":
        screenshot()
    elif args.command == "get_sign":
        get_sign(args)
    elif args.command == "get_apk":
        get_apk.get_apk(args)
    elif args.command == "wifi":
        wifi()
    elif args.command == "push_cert":
        push_cert(args)
    elif args.command == "ls":
        ls()
    elif args.command == "sign_info":
        sign_info(args)
    elif args.command == "public_key":
        public_key()


def sign_info(args):
    with tempfile.TemporaryDirectory() as tmp_dir:
        cert_full_path = os.path.join(tmp_dir, 'tmp.cert')
    # keytool -export -keystore keystore -storepass <your-keystore-password> -alias <your-alias> -file <certificate-file>.cer
        command_gen_cert = ['keytool', '-export','-keystore', args.path, '-storepass', args.pwd, '-alias', args.alias, '-file', cert_full_path]
        rst = subprocess.run(command_gen_cert, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        assert rst.returncode == 0
        command_get_md5 = ['openssl', 'x509', '-in', cert_full_path, '-noout', '-fingerprint', '-md5']
        rst = subprocess.run(command_get_md5, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        assert rst.returncode == 0

        output = rst.stdout
        match = re.search(r'Fingerprint=([A-F0-9:]+)', output)
        if match:
            md5_fingerprint = match.group(1)
            print("md5 finterprint:", md5_fingerprint.replace(":", ""))
        else:
            exit(1)

        command_get_public_key = ['openssl', 'x509', '-in', cert_full_path, '-pubkey', '-noout']
        rst = subprocess.run(command_get_public_key, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        match = re.search(r'-----BEGIN PUBLIC KEY-----\n([A-Za-z0-9+/=\n]+)\n-----END PUBLIC KEY-----', rst.stdout)
        if match:
            public_key = match.group(1)
            print("pubic key: ", public_key.replace("\n", ""))
        else:
            exit(1)


def ls():
    items = util.run_get_output("adb shell pm list packages -3")
    items: [str] = items.split("\n")
    pkgs = [item[len('package:'):] for item in items]
    print(items)
    pass


if __name__ == "__main__":
    main()
