import os


def add_git_ignore(path):
    exist = False
    if os.path.exists('.gitignore'):
        with open('.gitignore', 'r+') as f:
            for line in f.readlines():
                if path == line.strip():
                    exist = True
                    break

    with open('.gitignore', 'a+') as f:
        if not exist:
            f.write(path + '\n')
