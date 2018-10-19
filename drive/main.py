"""The entry point into the `drive` executable. Parses command-line arguments
and then dispatches to the proper function in sync.py.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: October 2018
"""
import argparse

from .sync import pull, push


def main():
    parser = argparse.ArgumentParser(description='Sync Google Drive files')
    parser.add_argument('action', choices=['push', 'pull'])
    # TODO: Multiple paths for push and pull commands.
    parser.add_argument('path', nargs='?', default='.')

    args = parser.parse_args()
    if args.action == 'pull':
        pull(args.path)
    else:
        pull(args.path)
