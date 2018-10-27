"""The main logic of the program: pushing and pulling files from Google Drive.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: October 2018
"""


def sync(service, folder, ignore_paths):
    """Synchronize the folder with Google Drive. First sync behaves exactly like
    `pull`. Subsequent syncs check for files that have changed since the last
    sync on either locally or remotely, and handles them as follows:

      - Files that have changed remotely are downloaded, whether or not they
        have changed locally.
      - Files that have changed locally but not remotely are uploaded.

    Any files that match a pattern in `ignore_paths` will not be uploaded or
    downloaded.
    """
    changeset = make_changeset(service, folder, ignore_paths)
    apply_changeset(service, changeset)


def push(service, folder, ignore_paths):
    """Make Google Drive identical to the folder. This operation will make no
    local changes, only remote ones.

    Any files that match a pattern in `ignore_paths` will not be uploaded.
    """
    raise NotImplementedError


def pull(service, folder, ignore_paths):
    """Make the folder identical to Google Drive. This operation will make no
    remote changes, only remote ones.

    Any files that match a pattern in `ignore_paths` will not be downloaded.
    """
    raise NotImplementedError


def make_changeset(service, folder, ignore_paths):
    raise NotImplementedError


def make_local_changeset(folder, ignore_paths, last_sync):
    pass


def make_remote_changeset(service, ignore_paths, last_sync):
    pass


def apply_changeset(service, changeset):
    """Apply the changeset. This operation may make both local and remote
    changes.
    """
    raise NotImplementedError
