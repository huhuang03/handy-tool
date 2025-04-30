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
    'gitup', 'done', 'gettopactivity', 'ip', 'merged_rm', 'gh1',
    'clean_space', 'du1', 'apktool1',
    'lg', 'utf8_2_utf8bom', 'sync_link', 'find_program',
    'rn_ex', 'json2bean', 'jt_code', 'remote', 'img',
    "where1", 'sy', 'junk_file', 'an_util', 'cmake1', 'path', 'pip1']

# 'jvm',
if is_windows():
    COMMANDS += ['jenv']

COMMAND_MAP = [
    ['au', "an_util"],
    ['md51', 'md5'],
    ['git1', 'git'],
    ['ro', 'repo'],
    ['file1', 'file']
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
    rst.append(_create_command('dcode', 'idea.idea_data_grip'))
    # # c is easy mistake click
    # rst.append(_create_command('s', 'idea.smart_idea'))
    rst.append(_create_command('pcode', 'idea.idea_pycharm'))
    rst.append(_create_command('rcode', 'idea.idea_rust_rover'))
    rst.append(_create_command('fcode', 'idea.idea_fleet'))
    rst.append(_create_command('ccode', 'idea.idea_clion'))
    rst.append(_create_command('vcpkg1', 'vcpkg1.vcpkg1'))
    rst.append(_create_command('cncode', 'idea.idea_clion_nova'))
    rst.append(_create_command('gcode', 'idea.idea_go_land'))
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
