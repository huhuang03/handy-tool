import os
import re
import subprocess
from ._util import get_top_package


def init_args(subparser):
    parse_get_apk = subparser.add_parser("get_apk", help="get apk by package name")
    parse_get_apk.add_argument("-p", type=str, help="print apk sign info")
    parse_get_apk.add_argument("-n", type=str, help="print apk sign info")


def get_apk(args):
    pkg_name = args.p
    app_name = args.n
    if pkg_name:
        rst = get_by_pkg_name(pkg_name)
        if rst:
            print("success extra apk")
            return
    elif app_name:
        pkg_name = get_pkg_by_app_name()
        rst = get_by_pkg_name(pkg_name)
        if rst:
            print("success extra apk")
            return
    else:
        top_package = get_top_package()
        if not top_package:
            print("can not find which pacakge to export")
            return
        rst = get_by_pkg_name(top_package)
        if rst:
            print("success extra apk")


def get_app_name_by_pkg():
    pass


def get_pkg_by_app_name(app_name):
    app_pkg_list = []
    for pkg_name in app_pkg_list:
        app_name = get_app_name_by_pkg(pkg_name)


def get_by_pkg_name(pkg_name: str):
    """
    true if find some.
    """
    commands = ["adb", "shell", "pm", "path", pkg_name]
    r_stdout = subprocess.run(commands, stdout=subprocess.PIPE).stdout
    if not r_stdout:
        return False
    apk_inner_path = r_stdout.decode("utf-8").strip()
    apk_inner_path = re.search(re.compile("package:(.*)"), apk_inner_path).group(1)

    output_name = f"{pkg_name}.apk"
    if os.path.exists(output_name):
        return False
    os.system(f"adb pull {apk_inner_path} {output_name}")
    return True
