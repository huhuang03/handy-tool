from handy_tool.util.util_os import is_windows
from setuptools import setup

PKG_NAME = 'handy_tool'


def create_console_script(*names):
    rst = []
    for name in names:
        rst.append(f'{name} = {PKG_NAME}.{name}:main')
    return rst


def _create_command(name, file_path):
    return f'{name} = {PKG_NAME}.{file_path}:main'


COMMANDS = [
    'gitup', 'done', 'gettopactivity', 'ip', 'merged_rm',
    'lg', 'utf8_2_utf8bom', 'save_space', 'find_program',
    'rn_ex', 'json2bean', 'jt_code', 'remote', 'file',
    'sy', 'junk_file', 'jvm', 'an_util', 'cm', 'path']

COMMAND_MAP = [
    ['au', "an_util"],
    ['g', 'git'],
    ['ro', 'repo']
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
    rst.append(_create_command('c', 'idea.smart_idea'))
    rst.append(_create_command('pcode', 'idea.idea_pycharm'))
    rst.append(_create_command('fcode', 'idea.idea_fleet'))
    rst.append(_create_command('ccode', 'idea.idea_clion'))
    rst.append(_create_command('icode', 'idea.idea_intellij'))
    rst.append(_create_command('wcode', 'idea.idea_webstorm'))
    rst.append(_create_command('hcode', 'idea.idea_phpstorm'))
    return rst


setup(
    name='handy tool',
    version='0.0.1',
    description='handy tool for daily use',
    entry_points={
        'console_scripts': _get_scripts()
    }
)
