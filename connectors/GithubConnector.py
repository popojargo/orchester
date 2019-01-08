from typing import AnyStr
from github import Github, Organization

from connectors.AbstractBaseConnector import AbstractBaseConnector


class GithubConnector(AbstractBaseConnector):

    def __init__(self, access_token: AnyStr, organization_id: AnyStr):
        self.org_id = organization_id
        self.access_token = access_token
        self.conn = Github(access_token)

    def get_organization(self) -> Organization.Organization:
        return self.conn.get_organization('')

    def get_user(self, username: AnyStr):
        return self.conn.get_user(username)

    def add_to_group(self, username: AnyStr):
        org = self.get_organization()
        if self.is_registered_to_group(username):
            return True

        user = self.get_user(username)
        return org.add_to_members(user, 'member')

    def remove_from_group(self, username: AnyStr):
        org = self.get_organization()
        if not self.is_registered_to_group(username):
            return True
        user = self.get_user(username)
        return org.remove_from_members(user)

    def is_registered_to_group(self, username: AnyStr):
        org = self.get_organization()
        user = self.get_user(username)
        return org.has_in_members(user)
