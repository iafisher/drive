"""The entry point into the `drive` executable. Parses command-line arguments
and then dispatches to the proper function in sync.py.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: October 2018
"""
import argparse

from .sync import init, pull, push


def main():
    parser = argparse.ArgumentParser(description='Sync Google Drive files')
    parser.add_argument('action', choices=['init', 'push', 'pull'])
    parser.add_argument('-d', '--dir', default='.')

    args = parser.parse_args()
    if args.action == 'init':
        init()
    elif args.action == 'pull':
        pull(args.dir)
    else:
        pull(args.dir)
