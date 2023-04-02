#!/usr/bin/env python
import sys
import os
from subprocess import call, check_output
import subprocess
import re


def main():
    pos = 0
    if len(sys.argv) == 2:
        pos = int(sys.argv[1])
    output = check_output(['adb', 'devices']).decode('utf-8')
    devices = output.split("\n")
    devices = [d for d in devices if d != '' and d != '\r']

    if len(devices) < 2:
        print("that's no devices connected")
    else:
        devices = devices[1:]
        if pos >= len(devices):
            print("that's only " + str(len(devices)) + " devices, and begin at 0")
        else:
            device = devices[pos]
            device = device.split('\t')[0]
            windows_output = check_output(['adb', 'shell', 'dumpsys activity activities | grep ResumedActivity']).decode('utf-8')
            rst_line = windows_output.splitlines()[0]
            m = re.match('.* (.*/\..*) ', rst_line)
            if m is not None:
                print(m.group(1))
            else:
                print(windows_output)