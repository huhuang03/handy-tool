# import subprocess as sp
import os
import subprocess


def run_admin_in_powershell(command):
    """
    Run command as root in powershell
    """
    # os.system(f'Powershell -Command "{command}"')
#     os.system(r'''
# Powershell -Command "& { Start-Process \"notepad.exe\"
#  -ArgumentList @(\"C:\\Windows\\System32\\drivers\\etc\\hosts\")
#  -Verb RunAs }" ''')
#     prog = sp.Popen(['runas', '/noprofile', '/user:Administrator', 'PowerShell.exe', '-Command', command], stdin=sp.PIPE)
#     prog.stdin.write(bytes(' ', 'utf-8'))
#     prog.communicate()

    subprocess.call(['runas', '/user:Administrator', 'PowerShell.exe'])
# subprocess.check_output('powershell Invoke-Command {cmd.exe -ArgumentList "/c netstat -nb"}', stdout=subprocess.PIPE, shell=True)
    # subprocess.check_output('powershell Start-Process netstat -ArgumentList "-nb" -Verb "runAs"', stdout=subprocess.PIPE, shell=True)
    # prog = sp.Popen(['runas', '/noprofile', '/user:Administrator', 'Notepad.exe'], stdin=sp.PIPE)
    # prog.stdin.write(bytes(' ', 'utf-8'))
    # prog.communicate()


def mklink(from_, to):
    """
    make a soft link
    """
    command = f'New-Item -Path {to} -ItemType SymbolicLink -Value {from_}'
    exit(f'For now, cal it manually: {command}')
    # run_admin_in_powershell()
