class Env:
    def __init__(self):
        pass

    def read(self):
        pass

    def java_clean(self):
        # so what java clean do?
        # first it find out all the java in path.
        # then prompt the user choice a java path.
        # then delete the java_path in path.
        # then it setup (and remember)? java_path
        # setup the JAVA_HOME and fix the path.
        pass


class Item:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        pass
