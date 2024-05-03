import argparse
import os
import subprocess
import tempfile
import zipfile
from pathlib import Path


def combine_jars(output_jar, *input_jars):
    with zipfile.ZipFile(output_jar, 'w') as out_zip:
        for jar_file in input_jars:
            print('jar_file: ', jar_file)
            with zipfile.ZipFile(jar_file, 'r') as in_zip:
                for file_info in in_zip.infolist():
                    # Exclude duplicate entries
                    if file_info.filename not in out_zip.namelist():
                        # Copy the file from input to output
                        out_zip.writestr(file_info, in_zip.read(file_info.filename))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('apk_path')
    parser.add_argument('--temp_dir', type=str, default='')
    args = parser.parse_args()
    apk_path = Path(args.apk_path)
    assert apk_path.exists() and apk_path.exists()
    # unzip to tmp directory
    if not args.temp_dir:
        temp_folder = tempfile.mkdtemp()
    else:
        temp_folder = args.temp_dir
        if not Path(temp_folder).exists():
            Path(temp_folder).mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(apk_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if '/' not in file_info.filename and file_info.filename.endswith('.dex'):
                zip_ref.extract(file_info, temp_folder)
    for f in os.listdir(temp_folder):
        if f.endswith('dex'):
            subprocess.run(['D:\\Program Files\\dex-tools-v2.4\\d2j-dex2jar.bat', f, '--force'], cwd=temp_folder)
    all_jar_file = [f for f in os.listdir(temp_folder) if f.endswith('.jar')]
    combine_jars('all.jar', *[Path(temp_folder, f).resolve().__str__() for f in all_jar_file])


if __name__ == '__main__':
    main()
