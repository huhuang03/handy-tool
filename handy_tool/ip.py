import requests
import os
import json


def try_baidu():
    pass


def try_ip_api():
    data = os.popen('curl http://ip-api.com/json/').read()


def main():
    try_ip_api()
    # data = os.popen('curl http://ip-api.com/json/').read()
    # if data == "":
    #     print("get no ip address")
    # else:
    #     data_json = json.loads(data)
    #     print(f'ip:{data_json["query"]}\ncountry: {data_json["country_name"]}')
