Pydrive is a simple utility to sync your files on Google Drive to and from your
Linux computer.

Pydrive supports the following operations:

```
$ pydrive sync
```

Synchronize `$PYDRIVE_HOME` with Google Drive. The first sync downloads
everything on Google Drive into `$PYDRIVE_HOME`. Subsequent syncs check for
files modified either locally on remotely since the last sync and updates them
as follows:

- If the file has only changed locally, then the file is uploaded to Google
  Drive.
- If the file has only changed remotely, then the file is downloaded into
  `$PYDRIVE_HOHE`.
- If the file has changed both locally and remotely, then the local version is
  replaced with the remote version.


```
$ pydrive push
```

Make your Google Drive identical to `$PYDRIVE_HOME`.


```
$ pydrive pull
```

Make `$PYDRIVE_HOME` identical to your Google Drive.


```
$ pydrive diff
```

Show the changes that `pydrive sync` would apply, without doing them.

## Configuration
Pydrive will ignore paths from `$PYDRIVE_HOME/.pydrive-ignore`. Ignored files
will not be uploaded from the disk or downloaded from the server.
