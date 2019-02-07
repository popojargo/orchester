from typing import AnyStr
from github import Github, Organization

from orchester.connectors import AbstractBaseConnector, normalize_exceptions


class GithubConnector(AbstractBaseConnector):

    def __init__(self, access_token: AnyStr, organization_id: AnyStr):
        self.org_id = organization_id
        self.access_token = access_token
        self.conn = Github(access_token)

    def get_organization(self) -> Organization.Organization:
        return self.conn.get_organization(self.org_id)

    def get_user(self, username: AnyStr):
        return self.conn.get_user(username)

    @normalize_exceptions
    def add_to_group(self, identifier: AnyStr):
        org = self.get_organization()
        if self.is_registered_to_group(identifier):
            return True

        user = self.get_user(identifier)
        org.add_to_members(user, 'member')
        return True

    @normalize_exceptions
    def remove_from_group(self, identifier: AnyStr):
        org = self.get_organization()
        if not self.is_registered_to_group(identifier):
            return True
        user = self.get_user(identifier)
        org.remove_from_members(user)
        return True

    @normalize_exceptions
    def is_registered_to_group(self, identifier: AnyStr):
        org = self.get_organization()
        user = self.get_user(identifier)
        return org.has_in_members(user)
