import os
import json


def main():
    data = os.popen('curl https://freegeoip.app/json/').read()
    if data == "":
        print("get no ip address")
    else:
        data_json = json.loads(data)
        print("ip: %s\ncountry: %s, city: %s" % (data_json["ip"], data_json["country_name"], data_json["city"]))
