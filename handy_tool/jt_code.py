import os

import requests
import pyperclip
import json

# IntelliJ IDEA 激活码 每日更新 长期提供【JetBrains全家桶】可用 - 白程序员的自习室
# https://www.studytime.xin/article/code.html

# 这个按道理说应该从公众号获取
PWD = "3527"
URL = f"https://api.studytime.xin/activationCode?passwd={PWD}"


def main():
    os.environ['NO_PROXY'] = 'api.studytime.xin'

    s = requests.Session()
    s.headers.update({
        "Referer": "https://www.studytime.xin/",
        "Origin": "https://www.studytime.xin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
    })

    content = s.get(URL).content
    j_content = json.loads(content)
    has_code = False
    if 'data' in j_content:
        code = j_content['data']
        has_code = bool(code)

    if not has_code:
        print(j_content);
        print("data is empty, maybe see https://www.studytime.xin/article/code.html")
        return
    print(code)
    print('already copied to system clipboard')
    pyperclip.copy(code)
