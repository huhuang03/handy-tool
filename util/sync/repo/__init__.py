from .add import add
from .repo_list import repo_list
from .state import state


def init_subparser(subparser):
    """
    Initial the subparser.
    @parm subparser the result of parser.Argparser().add_subparser()
    """
    repo_parser = subparser.add_parser("repo")
    repo_subparser = repo_parser.add_subparsers()

    add_parser = repo_subparser.add_parser('add')
    add_parser.set_defaults(func=add)

    list_parser = repo_subparser.add_parser('list')
    list_parser.set_defaults(func=repo_list)

    state_parser = repo_subparser.add_parser('state')
    state_parser.set_defaults(func=state)

    state_parser = repo_subparser.add_parser('st')
    state_parser.set_defaults(func=state)

    subparser.add_parser('sync')
