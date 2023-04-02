import os

from .app import App
from .env_home_win import CLION_HOME


def main():
    App(os.path.join(CLION_HOME, "bin", "clion64.exe"), "/Applications/CLion.app").start()
