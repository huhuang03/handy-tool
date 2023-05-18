#!/usr/bin/env python
from handy_tool.util.android import get_top_activity


def main():
    try:
        print(get_top_activity())
    except str:
        print("get top activity failed")
