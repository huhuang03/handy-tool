import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        command = ["adb", "logcat"]
    else:
        command = ["adb", "logcat", "-s", sys.argv[1]]

    subprocess.run(command)