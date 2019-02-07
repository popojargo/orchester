from typing import AnyStr
from slackclient import SlackClient

from orchester.connectors import AbstractBaseConnector, normalize_exceptions


class SlackConnector(AbstractBaseConnector):

    def __init__(self, token: AnyStr, legacy_token: AnyStr = ""):
        self.token = token
        self.legacy_conn = SlackClient(legacy_token)
        self.conn = SlackClient(token)

    def get_user(self, email: AnyStr):
        response = self.conn.api_call(
            "users.lookupByEmail",
            email=email
        )
        return response['user']

    @normalize_exceptions
    def add_to_group(self, identifier: AnyStr):
        if self.is_registered_to_group(identifier):
            return True

        response = self.legacy_conn.api_call(
            "users.admin.invite",
            email=identifier,
        )
        if response['ok']:
            return True
        else:
            raise ValueError('Failed to add user: {}'.format(response['error']))

    @normalize_exceptions
    def remove_from_group(self, identifier: AnyStr):
        if not self.is_registered_to_group(identifier):
            return True
        user = self.get_user(identifier)
        response = self.legacy_conn.api_call(
            'users.admin.setInactive',
            user=user['id']
        )
        if response['ok']:
            return True
        else:
            raise ValueError('Failed to remove user: {}'.format(response['error']))

    @normalize_exceptions
    def is_registered_to_group(self, identifier: AnyStr):
        response = self.conn.api_call(
            'users.list'
        )
        if not response['ok']:
            raise ValueError('Failed to remove user: {}'.format(response['error']))
        return any(('email' in x['profile'] and x['profile']['email']) == identifier for x in response['members'])
