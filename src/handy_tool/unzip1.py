import argparse
import os
from pathlib import Path

import argparse
import os
from pathlib import Path
from zipfile import ZipFile


def _get_how_many_file_in_first_level(zip_path: Path) -> int:
    """返回压缩包第一层的文件数量（不包含子文件夹里的文件）"""
    with ZipFile(zip_path, 'r') as zipf:
        # 获取所有文件路径，去掉文件夹路径
        files = [f for f in zipf.namelist() if not f.endswith('/')]
        # 提取第一层文件
        first_level = set(f.split('/')[0] for f in files)
        return len(first_level)


def _uncompress(src_zip: Path, target_dir: Path):
    """解压 zip 文件到目标目录"""
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    with ZipFile(src_zip, 'r') as zipf:
        zipf.extractall(target_dir)
    print(f"解压完成: {src_zip} -> {target_dir}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help="需要解压的 zip 文件路径")
    args = parser.parse_args()
    zip_path = Path(args.path)

    how_many = _get_how_many_file_in_first_level(zip_path)
    if how_many == 1:
        _uncompress(zip_path, Path(os.getcwd()))
    else:
        # 用压缩包名称作为文件夹名
        _uncompress(zip_path, Path(os.getcwd()) / zip_path.stem)
