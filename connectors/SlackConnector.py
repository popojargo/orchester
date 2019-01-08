from typing import AnyStr
from slackclient import SlackClient

from connectors.AbstractBaseConnector import AbstractBaseConnector


class SlackConnector(AbstractBaseConnector):

    def __init__(self, token: AnyStr,legacy_token: AnyStr = ""):
        self.token = token
        self.legacy_conn = SlackClient(legacy_token)
        self.conn = SlackClient(token)

    def get_user(self, username: AnyStr):
        response = self.conn.api_call(
            "users.lookupByEmail",
            email=username
        )
        return response['user']

    def add_to_group(self, username: AnyStr):
        if self.is_registered_to_group(username):
            return True

        response = self.legacy_conn.api_call(
            "users.admin.invite",
            email=username,
        )
        if response['ok']:
            return True
        else:
            raise ValueError('Failed to add user: {}'.format(response['error']))

    def remove_from_group(self, username: AnyStr):
        if not self.is_registered_to_group(username):
            return True
        user = self.get_user(username)
        response = self.legacy_conn.api_call(
            'users.admin.setInactive',
            user=user['id']
        )
        if response['ok']:
            return True
        else:
            raise ValueError('Failed to remove user: {}'.format(response['error']))

    def is_registered_to_group(self, username: AnyStr):
        response = self.conn.api_call(
            'users.list'
        )
        return any(('email' in x['profile'] and x['profile']['email']) == username for x in response['members'])
