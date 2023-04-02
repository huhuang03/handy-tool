import re
import os
import subprocess

_PORT = 5555


def wifi():
    """
    follow https://stackoverflow.com/questions/4893953/run-install-debug-android-applications-over-wi-fi
    adb via wifi
    """
    ip_output = subprocess.run(["adb", "shell", "ip -f inet addr show"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    ip = re.search(re.compile("inet (.*)/.*wlan0"), ip_output).group(1)
    """this not work because will reset immediately"""
    os.system(f"adb tcpip {_PORT}")
    os.system(f"adb connect {ip}:{_PORT}")
    print(ip)
