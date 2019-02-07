from __future__ import print_function

from typing import AnyStr

from orchester.connectors import AbstractBaseConnector, normalize_exceptions
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file google_drive_token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]


class GDriveConnector(AbstractBaseConnector):

    def __init__(self, credential_path: AnyStr, token_path: AnyStr, file_id: AnyStr):
        self.file_id = file_id
        store = file.Storage(token_path)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(credential_path, SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('drive', 'v3', http=creds.authorize(Http()))

    @normalize_exceptions
    def get_user_permission(self, email: AnyStr):
        file_perms = self.service.permissions().list(
            fileId=self.file_id,
            fields="permissions(id,emailAddress)"
        ).execute()
        for perm in file_perms['permissions']:
            if perm['emailAddress'] == email:
                return perm
        return None

    @normalize_exceptions
    def add_to_group(self, identifier: AnyStr):
        if self.is_registered_to_group(identifier):
            return True
        body = {
            'role': 'writer',
            'type': 'user',
            'emailAddress': identifier
        }
        self.service.permissions().create(fileId=self.file_id, body=body).execute()
        return True

    @normalize_exceptions
    def remove_from_group(self, identifier: AnyStr):
        user_perm = self.get_user_permission(identifier)
        if not user_perm:
            return True

        self.service.permissions().delete(
            fileId=self.file_id,
            permissionId=user_perm['id']
        ).execute()
        return True

    @normalize_exceptions
    def is_registered_to_group(self, identifier: AnyStr):
        user_perm = self.get_user_permission(identifier)
        return bool(user_perm)
