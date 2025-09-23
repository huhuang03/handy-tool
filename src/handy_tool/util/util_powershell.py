# import subprocess as sp
import subprocess


def reload_env_by_powershell():
    powershell_script = '''
    $path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    $calcedPath = [System.Environment]::ExpandEnvironmentVariables($path)
    $Env:path = $calcedPath
    '''
    try:
        subprocess.run(["powershell", "-Command", powershell_script], check=True)
        print("PowerShell 脚本执行成功。")
    except subprocess.CalledProcessError as e:
        print("Error:", e)


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

# subprocess.call(['runas', '/user:Administrator', 'PowerShell.exe'])
# subprocess.check_output('powershell Invoke-Command {cmd.exe -ArgumentList "/c netstat -nb"}', stdout=subprocess.PIPE, shell=True)
# subprocess.check_output('powershell Start-Process netstat -ArgumentList "-nb" -Verb "runAs"', stdout=subprocess.PIPE, shell=True)
# prog = sp.Popen(['runas', '/noprofile', '/user:Administrator', 'Notepad.exe'], stdin=sp.PIPE)
# prog.stdin.write(bytes(' ', 'utf-8'))
# prog.communicate()


def mklink(real_file, to):
    """
    make a soft link
    """
    command = f'New-Item -Path {to} -ItemType SymbolicLink -Value {real_file}'
    exit(f'For now, cal it manually: {command}')
    # run_admin_in_powershell()
