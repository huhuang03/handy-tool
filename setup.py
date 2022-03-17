from util.util import is_windows
from setuptools import setup
import os


def create_console_script(*names):
    rst = []
    for name in names:
        rst.append(f'{name} = util.{name}:main')
    return rst


def _create_command(name, file_path):
    return f'{name} = util.{file_path}:main'


def _create_jetbrains_command(name):
    return '{} = util.jet_brains:main'.format(name)


COMMANDS = [
    "gitup", 'done', "gettopactivity", "ip", "merged_rm",
    "lg", 'utf8_2_utf8bom', "save_space", 'find_program',
    'rn_ex', 'json2bean', 'jt_code', 'remote', 'file',
    'junk_file', 'jvm', 'an_util', 'cm', 'path']

COMMAND_MAP = [
    ['au', "an_util"],
    ['g', 'git'],
    ['sy', 'sync']
]


def _get_scripts():
    # why I need create this by hand??
    rst = create_console_script(*COMMANDS)
    for item in COMMAND_MAP:
        rst.append(_create_command(item[0], item[1]))
    if is_windows():
        rst.append(_create_command("l", "l"))
    rst.append(_create_command('personal', 'personal.personal'))
    rst.append(_create_command('vcode', 'idea.vs'))
    rst.append(_create_command('acode', 'idea.idea_android'))
    rst.append(_create_command('scode', 'idea.scode'))
    rst.append(_create_command('pcode', 'idea.idea_pycharm'))
    rst.append(_create_command('ccode', 'idea.idea_clion'))
    rst.append(_create_command('icode', 'idea.idea_intellij'))
    rst.append(_create_command('wcode', 'idea.idea_webstorm'))
    rst.append(_create_command('hcode', 'idea.idea_phpstorm'))
    return rst


setup(
    name='python shell util',
    version='1.0.0',
    description='shell 简单工具',
    entry_points={
        'console_scripts': _get_scripts()
    }
)
