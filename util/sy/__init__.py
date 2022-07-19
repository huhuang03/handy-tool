from util.util.util_os import is_windows, is_mac


def main():
    if is_windows():
        from .win import win_sync
        win_sync()
    elif is_mac():
        from .mac import mac_sync
        mac_sync()
    else:
        print("unsupport os")