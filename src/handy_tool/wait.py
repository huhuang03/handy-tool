# 10分钟check一次
import argparse
import subprocess

import requests
import time


def wait_for_url(url: str, interval: int = 600):
    """每隔 interval 秒检查一次 url，直到返回 200"""
    while True:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                print(f"[OK] {url} 可连通，返回 200")
                return
            else:
                print(f"[WARN] {url} 返回 {resp.status_code}，等待 {interval} 秒后重试")
        except Exception as e:
            print(f"[ERROR] 连接 {url} 失败: {e}，等待 {interval} 秒后重试")

        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()

    wait_for_url(args.url)
    subprocess.run(['done'])