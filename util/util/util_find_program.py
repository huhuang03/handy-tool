from typing import List, Iterator
import os


def get_folders_in_program_files(sub_folders: List[str]) -> List[str]:
    return [os.path.join(f, *(["Program Files"] + sub_folders)) for f in get_driver_paths()] \
           + [os.path.join(f, *(["Program Files (x86)"] + sub_folders)) for f in get_driver_paths()]


def get_driver_paths():
    """
    Find the driver that exist.
    """
    rst: List[str] = []
    for i in range(ord('A'), ord('Z')):
        dir_driver = f"{str(chr(i))}:\\"
        if os.path.exists(dir_driver):
            rst.append(dir_driver)
    return rst


# Find program in windows
# It will search program in X:\Program Files X:\Program Files(x86)
def _find_in_folder(folder_name, to_find) -> List[str]:
    rst = []
    to_find_low = to_find.lower()
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        for f in os.listdir(folder_name):
            if to_find_low in f.lower():
                rst.append(os.path.join(folder_name, f))
    else:
        pass
    return rst


def _find(disk_name, to_find):
    rst = []
    path = os.path.join(f"{disk_name}:\\", 'Program Files')
    rst += _find_in_folder(path, to_find)
    path = os.path.join(f"{disk_name}:\\", 'Program Files (x86)')
    rst += _find_in_folder(path, to_find)
    return rst


def find_program(program_part_name) -> List[str]:
    """
    may be not work now, use find_file??
    """
    if not os.name == 'nt':
        exit('only work on window')
    rst = []
    for i in range(ord('A'), ord('Z')):
        rst += _find(str(chr(i)), program_part_name)
    return rst


def find_file(part_name: List[str], in_program_folder: bool = True) -> str:
    """
    see find_files
    """
    return next(iter(find_files_iter(part_name, in_program_folder=in_program_folder)), '')


def find_files(part_name: List[str], in_program_folder: bool = True) -> List[str]:
    """
    @param part_name a list of sub folder
    @param in_program_folder True means find in Program Files and Program Files (x86)
    """
    return list(find_files_iter(part_name, in_program_folder=in_program_folder))


def find_files_iter(part_name: List[str], in_program_folder: bool = True) -> List[str]:
    for i in range(ord('A'), ord('Z')):
        dir_driver = f"{str(chr(i))}:\\"
        if in_program_folder:
            yield from _find_files_iter(["Program Files"] + part_name, dir_driver)
            yield from _find_files_iter(["Program Files (x86)"] + part_name, dir_driver)
        else:
            yield from _find_files_iter(part_name, dir_driver)


def _find_files_iter(part_name: List[str], cur_folder: str) -> Iterator[str]:
    if len(part_name) == 0:
        return

    if not os.path.exists(cur_folder):
        return

    cur_part = part_name[0]
    other_parts = part_name[1:]
    fit_files = [os.path.join(cur_folder, f) for f in os.listdir(cur_folder) if f == cur_part]

    if len(other_parts) == 0:
        yield from fit_files
    else:
        for fit_file in fit_files:
            if os.path.isdir(fit_file):
                yield from _find_files_iter(other_parts, fit_file)


def find_folder_in_program_files_by_file_name(file_name: List[str]) -> List[str]:
    # yield from _find_files_iter(["Program Files"] + part_name, dir_driver)
    # yield from _find_files_iter(["Program Files (x86)"] + part_name, dir_driver)
    return find_folder_by_file_name(
        get_folders_in_program_files([]),
        file_name
    )


def find_folder_by_file_name(folders: List[str], file_names: List[str]) -> List[str]:

    """
    How to judge the folder level?
    :return:
    """
    rst: List[str] = []
    for f in folders:
        for dirpath, dirnames, filenames in os.walk(f):
            if dirpath in rst:
                continue
            found = True
            for name in file_names:
                if name not in filenames:
                    found = False
                    break

            if found:
                rst.append(dirpath)
    rst = [f for f in rst if 'jre' not in f]
    return rst
