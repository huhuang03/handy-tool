from handy_tool.jt_code import main
from ..util.util import is_windows, is_mac
from .personal_win import setup_win

def main():
    if is_mac():
        print("only work in win")
    elif is_windows():
        setup_win() 
    else:
        print("unknown os")


# create by set_up.py has no name "__main__"
main()