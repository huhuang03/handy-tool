import os
import re

from .. import util as util_path

def run(args):
    # Namespace(command='list', l=False, func=<function run at 0x0000025C3C2EFD90>)
    if not args.l:
        print("\n".join(util_path.get_path_list()))
    else:
        path_list = util_path.get_path_list()
        rst = []
        re_env = re.compile('%(.+)%')
        for p in path_list:
            m = re_env.match(p)
            if m:
                env_key = m.group(1)
                env_value = os.environ[env_key] or env_key
                rst.append(f'{env_value}({p})')
            else:
                rst.append(p)
        print("\n".join(rst))

def init_parser(parser):
    parser.set_defaults(func=run)
    parser.add_argument("-l", action='store_true')