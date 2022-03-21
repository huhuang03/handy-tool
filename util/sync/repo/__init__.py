from .add import add


def init_subparser(subparser):
    """
    Initial the subparser.
    @parm subparser the result of parser.Argparser().add_subparser()
    """
    repo_parser = subparser.add_parser("repo")
    repo_subparser = repo_parser.add_subparsers()
    add_parser = repo_subparser.add_parser('add')
    add_parser.add_argument('-foo')
    # you can not called?
    add_parser.set_defaults(func=add)
    # how to call you?

    subparser.add_parser('list')
    subparser.add_parser('sync')
