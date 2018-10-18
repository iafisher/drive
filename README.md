**Use case**: You use Linux and want to sync your files on Google Drive to your
desktop. You don't like LibreOffice so you primarily use the web app to edit
your documents, but you want to have an offline copy for when you don't have
Internet access.

Many or most of your files are Google Docs, so [grive2] isn't an option.
[Insync] is nice but you don't want to pay for it. You can't seem to configure
the [drive][go-drive] or [rclone] CLI clients to do what you want.

## Set-up
1. Create a Google APIs project following [these instructions] substituting
   "Drive API" for "Blogger API."
2. Download a client secrets file and set the `PYDRIVE_CLIENT_SECRETS`
   environment variable to its location on your filesystem.
3. Clone this repository, activate the virtual environment and install
   dependencies (`pipenv shell`), and install the script
   (`python3 setup.py develop`).

## Usage
To be implemented.

[grive2]: https://github.com/vitalif/grive2
[Insync]: https://www.insynchq.com/downloads
[go-drive]: https://github.com/odeke-em/drive
[rclone]: https://rclone.org/
[these instructions]: http://www.datadependence.com/2016/03/google-python-library-oauth2/
