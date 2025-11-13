from typing import List
from pathlib import Path
from argparse import ArgumentParser
from ppadb.client import Client as AdbClient
from th_common import assert_folder_exists
import fnmatch


def main():
    parser = ArgumentParser()
    push_parser = parser.add_subparsers().add_parser("push")
    push_parser.add_argument("src", type=str)
    push_parser.add_argument("dest", type=str)
    push_parser.add_argument("--sync", action="store_true")
    push_parser.add_argument('--ignore-pattern', action='append', default=[],
                             help='Ignore file/dir pattern, can repeat')
    args = parser.parse_args()

    client = AdbClient(host='127.0.0.1', port=5037)
    devices = client.devices()
    if len(devices) > 1:
        raise 'there are many devices connected'
    if len(devices) == 0:
        raise 'there is no device connected'
    device = devices[0]

    remote_path = Path(args.dest).resolve()
    if not remote_exists_and_is_dir(device, remote_path.as_posix()):
        raise f'remote {remote_path} not exists or is not a folder'

    src_folder = Path(args.src).resolve()
    assert_folder_exists(src_folder)

    for f in src_folder.glob('*'):
        if should_ignore(f.relative_to(src_folder), args.ignore_pattern):
            print('ignore: ', f)
            continue
        dst_path = remote_path / f.relative_to(src_folder)

        try:
            print('check: ', f)
            remote_info = device.shell(f'stat -c "%s %Y" "{dst_path.as_posix()}"')
            remote_size, remote_mtime = map(int, remote_info.split())
        except Exception:
            remote_size, remote_mtime = None, None
        print(f'remote_size: {remote_size}, remote_time: {remote_mtime}')

    # remote_info = device.shell(f'stat -c "%s %Y" "{remote_path}"')
    # print(remote_info)


def remote_exists_and_is_dir(device, remote_path):
    """
    返回 (exists: bool, is_dir: bool)
    """
    # 注意要用 quotes 避免路径中空格问题
    cmd = f'test -e "{remote_path}" && echo exists || echo missing'
    exists_output = device.shell(cmd).strip()
    if exists_output != "exists":
        return False, False

    # 检查是否是目录
    cmd = f'test -d "{remote_path}" && echo dir || echo file'
    type_output = device.shell(cmd).strip()
    return True, type_output == "dir"


def should_ignore(path: Path, ignore_pattern: List[str]) -> bool:
    """
    path: 相对于 src_folder 的 Path
    """
    rel_path = str(path.as_posix())  # 转成 'a/b/c' 风格字符串
    for pattern in ignore_pattern:
        if pattern.endswith("/"):
            if rel_path == pattern[:-1] or rel_path.startswith(pattern):
                return True
        # 文件通配符匹配
        elif fnmatch.fnmatch(rel_path, pattern):
            return True
    return False
