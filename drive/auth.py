import os

import httplib2
from googleapiclient.discovery import build
from oauth2client import client, file


def get_credentials():
    """Return a credentials object that allows full access to a user's Google
    Drive account.

    Make sure to set the PYDRIVE_CLIENT_SECRETS environment variable to the
    location of the client secrets JSON file.

    If the user has not yet given permission to this app, then this function
    will prompt them to open a URL in a browser and copy a code back onto the
    command line.

    Mainly copied from http://www.datadependence.com/2016/03/google-python-library-oauth2/
    """
    scope = 'https://www.googleapis.com/auth/drive'
    flow = client.flow_from_clientsecrets(
        os.environ['PYDRIVE_CLIENT_SECRETS'], scope,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )
    storage = file.Storage('~/.pydrive')
    credentials = storage.get()

    if not credentials or credentials.invalid:
        auth_uri = flow.step1_get_authorize_url()
        print('Enter this URL in a browser:', auth_uri)
        auth_code = input('Enter the auth code: ')
        credentials = flow.step2_exchange(auth_code)
        storage.put(credentials)

    return credentials


def get_service():
    """Return an authenticated Drive client.

    If the user has not yet given permission to this app, then this function
    will prompt them to open a URL in a browser and copy a code back onto the
    command line.

    Mainly copied from http://www.datadependence.com/2016/03/google-python-library-oauth2/
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    return build('drive', 'v3', http=http)
