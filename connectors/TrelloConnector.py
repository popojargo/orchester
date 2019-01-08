from typing import AnyStr

from trello import trelloclient, member
from connectors.AbstractBaseConnector import AbstractBaseConnector


class TrelloConnector(AbstractBaseConnector):

    def __init__(self, api_key: AnyStr, api_secret: AnyStr, token: AnyStr, token_secret: AnyStr, org_id: AnyStr):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = trelloclient.TrelloClient(
            api_key=self.api_key,
            api_secret=self.api_secret,
            token=token,
            token_secret=token_secret
        )
        self.org_id = org_id

    def create_fake_member(self, username):
        """
        Since the client use the id to add the member to an organization, we create a member object with the username
        as an id.
        :param username:
        :return:
        """
        return member.Member(self.client, username)

    def get_organization(self):
        return self.client.get_organization(self.org_id)

    def add_to_group(self, username):
        if self.is_registered_to_group(username):
            return True

        org = self.get_organization()
        fake_member = self.create_fake_member(username)
        org.add_member(fake_member)
        return True

    def remove_from_group(self, username):
        if not self.is_registered_to_group(username):
            return True

        matched_member = self.get_member_by_username(username)
        if not matched_member:
            return False
        org = self.get_organization()
        org.remove_member(matched_member)
        return True

    def get_org_members(self):
        org = self.get_organization()
        return org.get_members()

    def get_member_by_username(self, username):
        members = self.get_org_members()
        for x in members:
            if x.username == username:
                return x
        return None

    def is_registered_to_group(self, username):
        members = self.get_org_members()
        return any(x.username == username for x in members)
