import os
import argparse


def find_missing_folder(path):
    # 把路径规范化为绝对路径
    path = os.path.abspath(path)

    # 逐层拆分路径，直到盘符或根目录
    parts = []
    while True:
        head, tail = os.path.split(path)
        if tail:
            parts.append(tail)
        else:
            if head:
                parts.append(head)
            break
        path = head
    parts.reverse()  # 现在 parts 是从盘符开始的各层路径

    # 从头开始拼接路径，检查是否存在
    current_path = parts[0]  # 例如 "D:\\"
    for folder in parts[1:]:
        current_path = os.path.join(current_path, folder)
        if not os.path.exists(current_path):
            return current_path  # 返回第一个不存在的目录或文件

    return None  # 全部存在

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('test_path')
    args = parser.parse_args()

    missing = find_missing_folder(args.test_path)
    if missing:
        print(f"第一个不存在的路径: {missing}")
    else:
        print("路径完整，所有文件夹均存在。")

if __name__ == "__main__":
    main()
