from enum import Enum
from typing import AnyStr
from orchester import connectors
import json

from orchester.ConfigHelper import pick
from orchester.Exceptions import ConfigEntryMissingError


class ConnectorType(Enum):
    GITHUB = 'github'
    TRELLO = 'trello'
    G_DRIVE = 'g_drive'
    G_GROUPS = 'g_groups'
    SLACK = 'slack'


SUPPORTED_CONNECTORS = ['github', 'trello', 'g_drive', 'slack']


class ConnectorManager:

    def __init__(self, config):
        self.default_connector = ""
        self.connectors = {}

        self.default_connector = pick(config, 'default_connector')
        if pick(config, 'connectors'):
            for key, connector_cfg in config['connectors'].items():
                if key not in SUPPORTED_CONNECTORS:
                    continue
                converted_key = ConnectorType(key)
                self.connectors[converted_key] = self.create_connector(key, connector_cfg)

    def create_connector(self, name, cfg):
        """
        Creates the connector according to their configuration
        :param name:
        :param cfg:
        :return:
        """
        if name == 'trello':
            return connectors.TrelloConnector(
                api_key=cfg['api_key'],
                api_secret=cfg['api_secret'],
                token=cfg['token'],
                token_secret=cfg['token_secret'],
                team_id=cfg['team_id']

            )
        elif name == 'github':
            return connectors.GithubConnector(
                access_token=cfg['token'],
                organization_id=cfg['org_id']
            )
        elif name == 'slack':
            return connectors.SlackConnector(
                token=cfg['token'],
                legacy_token=cfg['legacy_token']
            )
        elif name == 'g_drive':
            return connectors.GDriveConnector(
                token_path=cfg['token_path'],
                credential_path=cfg['credential_path'],
                file_id=cfg['file_id']
            )

    def add_to_group(self, connector_type: ConnectorType, identifier: AnyStr):
        if not connector_type in self.connectors:
            raise ConfigEntryMissingError('connectors.{}'.format(connector_type.value))
        return self.connectors[connector_type].add_to_group(identifier)

    def remove_from_group(self, connector_type: ConnectorType, identifier: AnyStr):
        if not connector_type in self.connectors:
            raise ConfigEntryMissingError('connectors.{}'.format(connector_type.value))
        return self.connectors[connector_type].remove_from_group(identifier)

    def is_registered_to_group(self, connector_type: ConnectorType, identifier: AnyStr):
        if not connector_type in self.connectors:
            raise ConfigEntryMissingError('connectors.{}'.format(connector_type.value))
        return self.connectors[connector_type].is_registered_to_group(identifier)
