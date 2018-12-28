# This repository is not finished and no longer maintained.

If you want a simple back-up of Google Drive onto your desktop, so you can
access your files offline, then all you need is to set up [rclone](https://rclone.org):

```shell
$ rclone config
```

And then run this one command:

```shell
$ rclone sync -P --drive-export-formats ods,odt,odp --exclude "/whatever/" drive: ~/Drive
```

Put it in your cronfile for a regular back-up.

Note that this is a one-way sync: it does not affect your files on Drive itself.
I haven't tried a two-way sync, but I would be wary as some format-scrambling is
likely.
