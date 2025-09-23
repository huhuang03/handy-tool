# not ready now, seems python function object can't judge args len?
class ArgPassSubCommandManager:
    def __init__(self, command_map):
        self.command_map = command_map

    def run(self, args):
        command = args.command
        if not command:
            exit('should have an sub command')
        fun = self.command_map['command']
        if not fun:
            exit(f"can't find command {command}")
        # get the fun
        if not type(fun) != 'function':
            exit(f"command {command} is not an function")

        # ok check the fun args len