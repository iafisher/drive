"""The main logic of the program: pushing and pulling files from Google Drive.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: October 2018
"""

import json
import os
import time


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
    last_sync = get_time_of_last_sync(folder)
    # Write the sync time BEFORE syncing.
    write_time_of_last_sync(folder)

    local_cset = get_local_changes(folder, ignore_paths, last_sync)
    remote_cset = get_remote_changes(service, ignore_paths, last_sync)

    # Ignore local changes to files that have also changed remotely.
    local_cset = {path for path in local_cset if path not in remote_cset}

    apply_remote_changeset(service, remote_cset)
    apply_local_changeset(local_cset)


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


def get_local_changes(folder, ignore_paths, last_sync):
    """Return a set of all files in the folder (except those matching a path in
    `ignore_paths`) that have changed since `last_sync`, which should be a
    timestamp in seconds.
    """
    changes = set()
    for path in ifiles(folder, ignore_path):
        sbuf = os.stat(path)
        if sbuf.st_mtime > last_sync:
            changes.add(path)
    return changes


def get_remote_changes(service, ignore_paths, last_sync):
    raise NotImplementedError


def apply_local_changeset(changeset):
    raise NotImplementedError


def apply_remote_changeset(service, changeset):
    raise NotImplementedError


def ifiles(folder, ignore_paths):
    """Iterate over all files in the folder recursively, skipped those that
    match a pattern in `ignore_paths`.
    """
    for path in glob.iglob(folder + '/**/*'):
        if all(not ignore_match(ipath, path) for ipath in ignore_path):
            yield path


def get_time_of_last_sync(folder):
    """Retrieve the time of last sync from the cache file. If no sync has been
    performed, or the cache file cannot be opened, None is returned.
    """
    try:
        with open(get_cache_path(folder), encoding='utf-8') as f:
            cache = json.load(f)
        return cache['last_sync']
    except:
        return None


def write_time_of_last_sync(folder):
    """Write the current time to the cache file so that the next call to
    `get_time_of_last_sync` will return it.
    """
    with open(get_cache_path(folder), 'w', encoding='utf-8') as f:
        json.dump({'last_sync': time.time()}, f)


def get_cache_path(folder):
    """Return the path to the cache file, relative to the given folder."""
    return os.path.join(folder, '.pydrive', 'cache')


def load_ignore_paths(folder):
    """Load a list of ignore paths from the .pydrive-ignore file in the given
    folder.
    """
    ignore_paths = []
    try:
        path = os.path.join(folder, '.pydrive-ignore')
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    continue
                elif line.startswith('/'):
                    # Absolute paths should be made relative to the folder.
                    ignore_paths.append(os.path.join(folder, line[1:]))
                else:
                    ignore_paths.append(line)
    except FileNotFoundError:
        pass
    except PermissionError:
        sys.stderr.write(
            'Warning: unable to open .pydrive-ignore because of permissions'
            ' error\n'
        )
    return ignore_paths


def ignore_match(ignore_path, path):
    """Return True if `path` matches the ignore path."""
    raise NotImplementedError
