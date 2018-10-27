"""Authentication with Google Drive's API.

Based on this guide:
    http://www.datadependence.com/2016/03/google-python-library-oauth2/

Author:  Ian Fisher (iafisher@protonmail.com)
Version: October 2018
"""
import os
import sys

import httplib2
from googleapiclient.discovery import build
from oauth2client import client, clientsecrets, file


def get_credentials(path_to_storage):
    """Return a credentials object that allows full access to a user's Google
    Drive account.

    `path_to_storage` is the path where the user's credentials will be stored.

    If the user has not yet given permission to this app, then this function
    will prompt them to open a URL in a browser and copy a code back onto the
    command line.
    """
    scope = 'https://www.googleapis.com/auth/drive'

    try:
        path_to_secrets = os.environ['PYDRIVE_CLIENT_SECRETS']
    except KeyError:
        sys.stderr.write(
            'Error: Please set $PYDRIVE_CLIENT_SECRETS to the location of the'
            ' secrets file for the pydrive application.\n'
        )
        sys.exit(2)

    try:
        flow = client.flow_from_clientsecrets(
            path_to_secrets,
            scope,
            redirect_uri='urn:ietf:wg:oauth:2.0:oob'
        )
    except clientsecrets.InvalidClientSecretsError:
        sys.stderr.write(
            'Error: invalid or missing file at $PYDRIVE_CLIENT_SECRETS\n'
        )
        sys.exit(2)

    storage = file.Storage(path_to_storage)
    credentials = storage.get()

    if not credentials or credentials.invalid:
        auth_uri = flow.step1_get_authorize_url()
        print('Enter this URL in a browser:', auth_uri)
        auth_code = input('Enter the auth code: ')
        credentials = flow.step2_exchange(auth_code)
        storage.put(credentials)

    return credentials


def get_service(path_to_storage):
    """Return an authenticated Drive client.

    `path_to_storage` is the path where the user's credentials will be stored.

    If the user has not yet given permission to this app, then this function
    will prompt them to open a URL in a browser and copy a code back onto the
    command line.
    """
    credentials = get_credentials(path_to_storage)
    http = credentials.authorize(httplib2.Http())
    return build('drive', 'v3', http=http)
