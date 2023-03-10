from .comm import save_repo_list
from handy_tool import util


def remove_all(args):
    confirm = util.confirm('Do you canfirm to delete all repos')
    if confirm:
        save_repo_list({})
