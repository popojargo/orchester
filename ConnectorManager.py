from enum import Enum
from typing import AnyStr
from connectors.GithubConnector import GithubConnector
from connectors.GDriveConnector import GDriveConnector
from connectors.SlackConnector import SlackConnector
from connectors.TrelloConnector import TrelloConnector
from dotenv import load_dotenv
import os

load_dotenv()


class ConnectorType(Enum):
    GITHUB = 'github'
    TRELLO = 'trello'
    G_DRIVE = 'g_drive'
    G_GROUPS = 'g_groups'
    SLACK = 'slack'


class ConnectorManager:

    def __init__(self):
        trello_api_key = os.getenv("TRELLO_API_KEY")
        trello_secret_key = os.getenv('TRELLO_API_SECRET')
        trello_token = os.getenv('TRELLO_TOKEN')
        trello_token_secret = os.getenv('TRELLO_TOKEN_SECRET')
        trello_org_id = os.getenv('TRELLO_ORG_ID')

        slack_token = os.getenv('SLACK_TOKEN')
        slack_legacy_token = os.getenv('SLACK_LEGACY_TOKEN')

        github_personal_key = os.getenv('GITHUB_OAUTH')
        github_org_id = os.getenv('GITHUB_ORG_ID')

        gdrive_file_id = os.getenv('GDRIVE_FILE_ID')

        self.connectors = {
            ConnectorType.GITHUB: GithubConnector(
                github_personal_key,
                github_org_id
            ),
            ConnectorType.G_DRIVE: GDriveConnector(
                gdrive_file_id
            ),
            ConnectorType.TRELLO: TrelloConnector(
                trello_api_key,
                trello_secret_key,
                trello_token,
                trello_token_secret,
                trello_org_id
            ),
            ConnectorType.SLACK: SlackConnector(
                slack_token,
                slack_legacy_token
            ),
        }

    def add_to_group(self, connector_type: ConnectorType, username: AnyStr):
        return self.connectors[connector_type].add_to_group(username)

    def remove_from_group(self, connector_type: ConnectorType, username: AnyStr):
        return self.connectors[connector_type].remove_from_group(username)

    def is_registered_to_group(self, connector_type: ConnectorType, username: AnyStr):
        return self.connectors[connector_type].is_registered_to_group(username)
