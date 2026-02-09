import argparse
from pathlib import Path
from dotenv import load_dotenv
import re
import os


def main():
    # usage: docker1 xx.compose.yaml [yy.compose.yaml]
    parser = argparse.ArgumentParser()
    parser.add_argument('src', type=str, help='the source compose file')
    parser.add_argument('dst', type=str, help='the destination compose file')
    args = parser.parse_args()
    src_path_str = args.src
    dst_path_str = args.dst
    src_path = Path(src_path_str)
    assert src_path.exists()
    src_content = src_path.read_text(encoding='utf-8')
    load_dotenv()

     # 正则匹配 ${VAR_NAME}
    pattern = re.compile(r'\$\{([A-Za-z0-9_]+)\}')

    replaced_vars = {}
    skipped_vars = set()

    def replace_var(match):
        var_name = match.group(1)
        # 优先用系统环境变量，其次.env
        value = os.environ.get(var_name)
        if value is not None:
            replaced_vars[var_name] = value
            return value
        else:
            skipped_vars.add(var_name)
            return match.group(0)  # 保持原样

    # 执行替换
    dst_content = pattern.sub(replace_var, src_content)

    # 打印信息
    if replaced_vars:
        print("Replaced variables:")
        for k, v in replaced_vars.items():
            print(f"  {k} = {v}")

    if skipped_vars:
        print("Skipped variables (not found):")
        for k in skipped_vars:
            print(f"  {k}")

    dst_path = Path(dst_path_str)
    dst_path.write_text(dst_content, encoding='utf-8')
    print(f"Written replaced content to {dst_path}")


if __name__ == '__main__':
    main()
