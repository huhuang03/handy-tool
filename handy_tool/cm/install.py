from ..util.util_git import add_git_ignore
import os
import pathlib


def _install(output_dir: str, is_32: bool = False):
    pathlib.Path(output_dir).mkdir(exist_ok=True)
    cmake_init_command = 'cmake ..'
    if is_32:
        cmake_init_command += ' -A win32'
    commands = [
        'cd build32',
        cmake_init_command,
        'cmake --build . --config Release --target install',
    ]
    commands += ['cmake --build . --config Debug --target install']

    commands += ['cd ..']
    commands_str = "&".join(commands)
    os.system(commands_str)


def _install64():
    _install('_cm_build', is_32=False)


def _install32():
    _install('_cm_build32', is_32=True)


def install(args):
    add_git_ignore('*build*/')
    i_32 = args.install_32
    i_64 = args.install_64
    if not i_32 and not i_64:
        i_32 = True
        i_64 = True
    if i_32:
        _install32()
    if i_64:
        _install64()
