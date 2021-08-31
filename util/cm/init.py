from ..util.util_git import add_git_ignore
import os
import pathlib


def install(args):
    # how can we do the install?
    add_git_ignore('*build*/')
    pathlib.Path('build32').mkdir(exist_ok=True)
    commands = [
        'cd build32',
        'cmake .. -A win32',
        'cmake --build . --config Release --target install',
    ]
    if args.build_debug:
        commands += ['cmake --build . --config Debug --target install']

    commands += ['cd ..']
    commands_str = "&".join(commands)
    print(commands_str)
    # os.system()

