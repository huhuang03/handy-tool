import requests
import os
import json


def try_baidu():
    pass


def try_ip_api():
    data = os.popen('curl http://ip-api.com/json/').read()
    print(data)


def main():
    try_ip_api()
