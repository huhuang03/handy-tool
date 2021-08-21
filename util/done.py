from .util.util import is_windows
import subprocess


def main():
    if not is_windows():
        exit("only work on win for now")
    subprocess.run(['powershell', '-Command', f'$wshell = New-Object -ComObject Wscript.Shell;$wshell.Popup("Done")'])


if __name__ == '__main__':
    main()
