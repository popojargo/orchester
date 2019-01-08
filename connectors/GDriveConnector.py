from __future__ import print_function

from typing import AnyStr

from connectors.AbstractBaseConnector import AbstractBaseConnector
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file google_drive_token.json.
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'


class GDriveConnector(AbstractBaseConnector):

    def __init__(self,file_id: AnyStr):
        self.file_id = file_id
        store = file.Storage('google_drive_token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('google_drive_credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('drive', 'v3', http=creds.authorize(Http()))

    def add_to_group(self, username: AnyStr):
        org = self.get_organization()
        if self.is_registered_to_group(username):
            return True
        return org.add_to_members(username, "member")

    def remove_from_group(self, username: AnyStr):
        org = self.get_organization()
        if not self.is_registered_to_group(username):
            return True
        return org.remove_from_members(username)

    def get_folder_permissions(self):
        return self.service.permissions().list(self.file_id)

    def get_member_permission_id(self, email: AnyStr):
        return self.service.permissions().getIdForEmail(email).id

    def is_registered_to_group(self, username: AnyStr):
        member_perm_id = self.get_member_permission_id(username)
        member_permission = self.service.permissions().get(self.file_id, member_perm_id)
        if not member_permission:
            return False
        return True
