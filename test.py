#!/usr/bin/env python3

from pathlib import Path
import unittest

import xld_logchecker

TESTS = [
    (Path('logs/not_real.log'), {'message': 'error: cannot open file', 'status': 'ERROR'}),
    (Path('logs/01.log'), {'message': 'OK', 'status': 'OK'}),
    (Path('logs/02.log'), {'message': 'OK', 'status': 'OK'}),
    (Path('logs/03.log'), {'message': 'Malformed', 'status': 'BAD'}),
    (Path('logs/04.log'), {'message': 'Not a logfile', 'status': 'ERROR'})
]

class TestLogchecker(unittest.TestCase):
    def test_logs(self):
        for log_file, expected in TESTS:
            with self.subTest(log=str(log_file)):
                actual = xld_logchecker.parse_log(log_file)
                self.assertEqual(expected, actual) 


if __name__ == "__main__":
    unittest.main()
