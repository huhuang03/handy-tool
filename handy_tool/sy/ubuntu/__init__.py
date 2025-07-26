import os
from pathlib import Path
from typing import Optional


from ..comm import git_sync, copytree_with_overwrite
from ..util import insert_source_command

generated_rc = Path('~/.sy/generated.zshrc').expanduser()
generated_rc.parent.mkdir(parents=True, exist_ok=True)


def _find_android_home() -> Optional[Path]:
    to_check = Path('~/Android/Sdk').expanduser()
    if to_check.exists():
        return to_check
    return None


def _handle_android_home():
    print('begin handle ANDROID_HOME')
    origin_android_home = os.environ.get('ANDROID_HOME')
    if not origin_android_home or not Path(origin_android_home).is_dir():
        print('not set android_home, begin to smart check')
        found = _find_android_home()
        if found is not None:
            origin_android_home = found.as_posix()
    _append_generated_rc('export ANDROID_HOME={}'.format(origin_android_home))

def _clear_generated_rc():
    generated_rc.write_text('', encoding='utf-8')

def _append_generated_rc(text: str):
    src = generated_rc.read_text(encoding='utf-8')
    generated_rc.write_text(src + '\n' + text, encoding='utf-8')

def _sync_sy():
    src = Path(__file__).parent / 'asset/'
    copytree_with_overwrite(src, Path('~/.sy/').expanduser())
    insert_source_command(Path('~/.zshrc').expanduser(), '. "$HOME/.sy/sy.zshrc"')

def ubuntu_sync():
    git_sync()
    _clear_generated_rc()
    _handle_android_home()
    _sync_sy()
