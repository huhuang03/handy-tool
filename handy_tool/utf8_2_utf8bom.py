import sys
import os


def main():
    folder = "."
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    folder = os.path.abspath(folder)
    if not os.path.exists(folder) or not os.path.isdir(folder):
        exit(f"{folder} folder not exist")

    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            full_path = os.path.join(dirpath, f)
            if full_path.endswith(".cpp") or full_path.endswith(".c") or full_path.endswith(".h"):
                print(f'begin parse file: {full_path}')
                with open(full_path, 'rb') as f:
                    raw_content = open(full_path, 'rb').read()
                str_content = raw_content.decode('utf-8-sig')
                sig_raw_content = str_content.encode('utf-8-sig')
                open(full_path, 'wb').write(sig_raw_content)



if __name__ == "__main__":
    main()