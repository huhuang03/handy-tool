from pathlib import Path

_cur_folder = Path('.')

_content = '''
{
  "default-registry": {
    "kind": "git",
    "baseline": "master",
    "repository": "https://github.com/microsoft/vcpkg"
  },
  "registries": [
    {
      "kind": "artifact",
      "location": "https://github.com/microsoft/vcpkg-ce-catalog/archive/refs/heads/main.zip",
      "name": "microsoft"
    }
  ]
}
'''

_cmake_preset_content = '''
{
  "version": 3,
  "configurePresets": [
    {
      "name": "default",
      "binaryDir": "${sourceDir}/build",
      "cacheVariables": {
        "CMAKE_TOOLCHAIN_FILE": "$env{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake",
        "CMAKE_INSTALL_PREFIX": "D:/Program Files"
      }
    }
  ]
}
'''


def preset():
    pass


def main():
    # vcpkg-configuration.json
    file_name = 'CMakePresets.json'
    dst_file = _cur_folder / file_name
    if dst_file.exists():
        print(f'{file_name} already exists')
        return
    dst_file.write_text(_cmake_preset_content, encoding='utf-8')
