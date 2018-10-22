"""Pydrive: simple Google Drive syncing on Linux.

Usage:
    pydrive push [path]
    pydrive pull [path]
    pydrive -h | --help

Options:
    -h --help   Show this screen.
"""
from docopt import docopt

from .sync import pull, push


def main():
    args = docopt(__doc__)
    if args['push']:
        pull(args['path'])
    elif args['pull']:
        pull(args['path'])
