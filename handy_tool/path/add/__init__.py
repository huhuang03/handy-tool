from ..user_scope import user_scope
from ...util.util import ensure_is_win


def add():
    ensure_is_win()
    user_scope.add_cwd_to_path()
