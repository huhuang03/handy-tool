import os
from subprocess import check_output


def push_cert(args):
    src_cert_path = args.cert_file_path
    src_cert_path = os.path.abspath(src_cert_path)
    if not os.path.exists(src_cert_path):
        exit(f'{src_cert_path} not exist, please check')
    # ok we need rename it.
    output = check_output(['openssl', 'x509', '-subject_hash_old', '-in', src_cert_path]).decode('utf-8')
    hash_code = (output.split("\n")[0]).strip()
    cert_file_name = f'{hash_code}.0'
    renamed_cert_path = os.path.join(os.path.dirname(src_cert_path), cert_file_name)
    origin_file_name = os.path.basename(src_cert_path)
    if origin_file_name != cert_file_name:
        print(f"Please notice that I have renamed {src_cert_path} to {renamed_cert_path}")
        os.rename(src_cert_path, renamed_cert_path)
    os.system(f'adb push {renamed_cert_path} /sdcard/{cert_file_name}')

    # ok, read write the storage.
    command = f"adb shell su -c 'mount -o rw,remount /'"
    os.system(command)

    command = f"adb shell su -c 'cp /sdcard/{cert_file_name} /system/etc/security/cacerts/'"
    os.system(command)
    os.system(f"adb shell su -c 'chmod 644 /system/etc/security/cacerts/{cert_file_name}'")

    command = f"adb shell su -c 'mount -o ro,remount /'"
    os.system(command)
