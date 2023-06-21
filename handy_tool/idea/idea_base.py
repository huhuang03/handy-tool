import os
import sys


class IdeaBase:
    def run(self, file_path):
        raise Exception("Please impl")

    def main(self):
        if len(sys.argv) < 2:
            file_path = '.'
        else:
            file_path = sys.argv[1]
        if not os.path.exists(file_path):
            exit('for now, I didn\'t think well how to handle directory not exist')
        self.run(file_path)