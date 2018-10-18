"""The main logic of the program: pushing and pulling files from Google Drive.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: October 2018
"""


def init(path):
    """Prompt the user with a URL to give the application access to their
    Google Drive, and initialize the directory at `path` with a .pydrive file
    containing the user's credentials.
    """
    pass


def push(path):
    """Push local changes at `path` to the cloud.

    `path` may point to a file or a directory. For directories, pushing is
    recursive: all sub-directories, sub-sub-directories etc. are pushed.

    If the local and remote versions of a file differ, then the remote version
    will be overwritten with the local version. If the versions do not differ,
    then no upload is performed.
    """
    pass


def pull(path):
    """Pull remote changes at `path` from the cloud.

    `path` may point to a file or a directory. For directories, pulling is
    recursive: all sub-directories, sub-sub-directories etc. are pulled.

    If the local and remote versions of a file differ, then the local version
    will be overwritten with the remote version. If the versions do not differ,
    then no download is performed.
    """
    pass
