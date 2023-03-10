import os
import json


def _init_windows_terminal():
    origin_folder = os.path.expanduser("~/AppData/Local/Packages/")
    for f in os.listdir(origin_folder):
        if f.startswith("Microsoft.WindowsTerminal"):
            origin_folder = os.path.join(origin_folder, f, 'LocalState')
            break
    setting_file = os.path.join(origin_folder, 'settings.json')
    if not os.path.exists(setting_file):
        exit("why can't find windows.terminal settings.json")
    # parse you!
    with open(setting_file) as f:
        json_setting = json.loads(f.read())
    old_actions = json_setting['actions']
    has_changed = False

    def add_action(n_key, n_action, force=False):
        nonlocal has_changed
        has_changed = False
        contains = False
        for action in old_actions:
            if action.keys == n_key:
                contains = True
                break
        if not contains or force:
            has_changed = True
            old_actions.append({
                "keys": n_key,
                "command": n_action
            })
    add_action("ctrl+w", "closeTab", True)
    add_action("ctrl+t", "newTab")
    add_action("shift+alt+}", "nextTab")
    add_action("shift+alt+{", "prevTab")
    if has_changed:
        with open(setting_file, 'w') as f:
            if not f.writable():
                return
            f.write(json.dumps(json_setting, indent=4))