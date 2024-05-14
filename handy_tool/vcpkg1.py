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


def main():
    preset_file = _cur_folder / 'vcpkg-configuration.json'
    if preset_file.exists():
        print('vcpkg-configuration.json already exists')
        return
    preset_file.write_text(_content, encoding='utf-8')
    print('done!')
