from pathlib import Path
import os
import json

from orchester.Exceptions import ConfigFileNotFoundError, ConfigEntryMissingError


def get_config_path():
    home = str(Path.home())
    config_filename = '.orchester.json'
    default_user_path = os.path.join(home, config_filename)
    default_cwd_path = os.path.join(os.getcwd(), config_filename)
    user_defined_cfg_path = os.getenv('ORCHESTER_CONFIG_PATH')

    if user_defined_cfg_path:
        return user_defined_cfg_path
    elif os.path.exists(default_cwd_path):
        return default_cwd_path
    else:
        return default_user_path


def get_config_data():
    config_path = get_config_path()

    if not os.path.exists(config_path):
        raise ConfigFileNotFoundError()
    with open(config_path) as f:
        return json.load(f)


def pick(obj, path):
    paths = path.split('.')
    cursor = obj
    curr_path = []
    for key in paths:
        curr_path.append(key)
        if key in cursor:
            cursor = cursor[key]
        else:
            raise ConfigEntryMissingError('.'.join(curr_path))
    return cursor
