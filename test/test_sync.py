import unittest
from io import StringIO
from unittest.mock import patch

from drive.sync import get_time_of_last_sync, ifiles, load_ignore_paths


class UtilitiesTest(unittest.TestCase):
    def test_ifiles(self):
        # Compare with a set as the order of the listing is not guaranteed.
        self.assertEqual(
            set(ifiles('./test/assets', [])), 
            {
                './test/assets/filetree/a.txt', './test/assets/filetree/b.txt',
                './test/assets/filetree/d', './test/assets/filetree/d/c.txt',
                './test/assets/filetree',
            }
        )

    def test_load_ignore_paths(self):
        sio = StringIO('''
            # A comment

            relpath
            /abspath
        ''')
        patched_open = lambda *args, **kwargs: sio
        with patch('drive.sync.open', new=patched_open):
            self.assertEqual(
                load_ignore_paths('./Drive'), ['relpath', './Drive/abspath']
            )

    def test_get_time_of_last_sync(self):
        sio = StringIO('{\"last_sync\": 123456}')
        patched_open = lambda *args, **kwargs: sio
        with patch('drive.sync.open', new=patched_open):
            self.assertEqual(get_time_of_last_sync('.'), 123456)
