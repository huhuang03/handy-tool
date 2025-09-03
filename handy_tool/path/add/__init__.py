from ..user_scope import user_scope
from ...util.util import ensure_is_win


def add():
    """
    this already check has added before add
    :return:
    """
    ensure_is_win()
    user_scope.add_cwd_to_path()
