from typing import AnyStr


class RequestFailedError(Exception):
    def __init__(self, error_description: AnyStr):
        # Call the base class constructor with the parameters it needs
        super(RequestFailedError, self).__init__("The request failed: {}".format(error_description))


class ConfigFileNotFoundError(Exception):
    def __init__(self):
        msg = """Config file not found.\n
You must either create a .orchester.json file in your home folder, create a .orchester.json file in your current
working directory or set a path to your configuration through the ORCHESTER_CONFIG_PATH environment variable.
"""
        super(ConfigFileNotFoundError, self).__init__(msg)


class ConfigEntryMissingError(Exception):
    def __init__(self, entry: AnyStr):
        msg = """The following entry is missing in the configuration file: {}.
Be sure to respect the .orchester.json template.""".format(entry)
        super(ConfigEntryMissingError, self).__init__(msg)
