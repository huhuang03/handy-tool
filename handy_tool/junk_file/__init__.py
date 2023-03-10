import argparse
import datetime
import re


def _parse_size(size_str) -> int:
    """
    parse the size_str to size(unit m)
    """
    r = re.compile(r'((\d*)[Gg])?(\d*)[Mm]?')
    m = r.match(size_str)
    g = m.groups()
    if len(g) == 3:
        g_size = g[1]
        m_size = g[2]
        rst = 0
        if m_size is not None and len(m_size) > 0:
            rst += int(m_size)
        if g_size is not None and len(g_size) > 0:
            rst += 1024 * int(g_size)
        return rst
    return 0


def _format_size(size: int) -> str:
    g = size // 1024
    m = size % 1024
    rst = ''
    if m:
        rst += str(m) + 'M'
    if g:
        rst = f'{g}G{rst}'
    return rst


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("size")
    args = parser.parse_args()
    size_str = args.size
    size = _parse_size(size_str)
    print(f'begin to crate {_format_size(size)} junk file')
    file_name = str(datetime.datetime.now()).replace(':', '_') + '_junk_file.tmp'

    # better write method?
    # write 1M per

    one_m_data = bytes([0x1]) * 1024 * 1024
    with open(file_name, 'wb') as f:
        index = 0
        while index < size:
            f.write(one_m_data)
            index += 1
    print('done!')
