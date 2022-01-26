# ok, read th setting.
import os.path

import yaml

_cached_settings = None


def settings():
    global _cached_settings
    if not _cached_settings:
        with open(os.path.join(os.path.dirname(__file__), 'settings.yml')) as f:
            _cached_settings = yaml.safe_load(f)
    return _cached_settings
