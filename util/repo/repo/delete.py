from .comm import save_repo_list
from ...sy import util


def delete(args):
    # need config
    confirm = util.confirm('Do you canfirm to delete all repos')
    if confirm:
        save_repo_list({})
