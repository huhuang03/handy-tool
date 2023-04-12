#!/usr/bin/env python
import sys
import os
from subprocess import call, check_output
import subprocess
import re
from handy_tool.util.android import get_top_activity


def main():
    try:
        print(get_top_activity())
    except str:
        print("get top activity failed")
