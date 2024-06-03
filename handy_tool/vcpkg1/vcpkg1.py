import argparse
from pathlib import Path

_cur_folder = Path('..')

_cmake_preset_content = '''
{
  "version": 2,
  "configurePresets": [
    {
      "name": "default",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/build",
      "cacheVariables": {
        "CMAKE_TOOLCHAIN_FILE": "$env{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
      }
    }
  ]
}
'''

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


def preset(args):
    pass


def overlay(args):
    pass


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.required = True
    parser_preset = subparsers.add_parser('preset')
    parser_preset.set_defaults(func=preset)
    parser_overlay = subparsers.add_parser('overlay')
    parser_overlay.set_defaults(func=overlay)
    args = parser.parse_args()
    print(args)

    # parser.add_argument('-custom', action=argparse.BooleanOptionalAction, default=True)
    # preset_file = _cur_folder / 'vcpkg-configuration.json'
    # if preset_file.exists():
    #     print('vcpkg-configuration.json already exists')
    #     return
    # preset_file.write_text(_content, encoding='utf-8')
    # print('done!')
