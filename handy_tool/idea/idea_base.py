import argparse


class IdeaBase:
    def run(self, args):
        raise Exception("Please impl")

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-p', help='print path', action=argparse.BooleanOptionalAction)
        parser.add_argument('path', help="project path", nargs='?')
        args = parser.parse_args()
        if not args.p and not args.path:
            args.path = '.'
        self.run(args)