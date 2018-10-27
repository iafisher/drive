"""Pydrive: simple Google Drive syncing on Linux.

Usage:
    pydrive sync
    pydrive diff
    pydrive push
    pydrive pull
    pydrive -h | --help

Options:
    -h --help   Show this screen.
"""
import os
import sys

from docopt import docopt

from . import auth, sync


def main():
    args = docopt(__doc__)
    if args['sync']:
        sync_cli()
    elif args['diff']:
        diff_cli()
    elif args['push']:
        push_cli()
    elif args['pull']:
        pull_cli()


def sync_cli():
    """A wrapper around sync.sync that initializes all its arguments from the
    user's pydrive configuration.
    """
    service, pydrive_home, ignore_paths = get_config()
    sync.sync(service, pydrive_home, ignore_paths)


def diff_cli():
    """A wrapper around sync.diff that initializes all its arguments from the
    user's pydrive configuration.
    """
    service, pydrive_home, ignore_paths = get_config()
    changeset = sync.make_changeset(service, pydrive_home, ignore_paths)
    # TODO: Print in a more readable format.
    print(changeset)


def pull_cli():
    """A wrapper around sync.pull that initializes all its arguments from the
    user's pydrive configuration.
    """
    service, pydrive_home, ignore_paths = get_config()
    sync.pull(service, pydrive_home, ignore_paths)


def push_cli():
    """A wrapper around sync.push that initializes all its arguments from the
    user's pydrive configuration.
    """
    service, pydrive_home, ignore_paths = get_config()
    sync.push(service, pydrive_home, ignore_paths)


def get_config():
    """Return the tuple (service, pydrive_home, ignore_paths), where `service`
    is a Google Drive client object, `pydrive_home` is the path to the local
    Drive folder, and `ignore_paths` is a list of paths to ignore.
    """
    try:
        folder = os.environ['PYDRIVE_HOME']
    except KeyError:
        sys.stderr.write(
            'Error: Please set $PYDRIVE_HOME to the path to the folder that you'
            ' wish to use.\n'
        )
        sys.exit(2)

    # Make sure that the .pydrive folder exists under $PYDRIVE_HOME.
    try:
        os.mkdir(os.path.join(folder, '.pydrive'))
    except FileExistsError:
        pass

    # Initialize the Google Drive service.
    creds_path = os.path.join(folder, '.pydrive', 'credentials.json')
    service = auth.get_service(creds_path)

    ignore_paths = sync.load_ignore_paths(folder)

    return (service, folder, ignore_paths)
