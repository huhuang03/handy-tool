import re
from subprocess import check_output


def get_top_activity():
    """
    should I raise exception?
    """
    output = check_output(['adb', 'devices']).decode('utf-8')
    devices = output.split("\n")
    devices = [d for d in devices if d != '' and d != '\r']

    if len(devices) < 2:
        raise "that's no devices connected"

    windows_output = check_output(['adb', 'shell', 'dumpsys activity activities | grep ResumedActivity']).decode('utf-8')
    rst_line = windows_output.splitlines()[0]
    rst_line = rst_line.strip()
    m = re.match('.* (.*/\..*) ', rst_line)
    if m is not None:
        return m.group(1)
    return ''
