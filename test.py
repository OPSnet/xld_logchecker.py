#!/usr/bin/env python3

from pathlib import Path
import unittest

import xld_logchecker

TESTS = [
    (
        Path("logs/not_real.log"),
        {"message": "error: cannot open file", "status": "ERROR"},
    ),
    (Path("logs/01.log"), {"message": "OK", "status": "OK"}),
    (Path("logs/02.log"), {"message": "OK", "status": "OK"}),
    (Path("logs/03.log"), {"message": "Malformed", "status": "BAD"}),
    (Path("logs/04.log"), {"message": "Not a logfile", "status": "ERROR"}),
    (Path("logs/05.log"), {"message": "OK", "status": "OK"}),
    (Path("logs/06.log"), {"message": "OK", "status": "OK"}),
    (Path("logs/07.log"), {"message": "Not a logfile", "status": "ERROR"}),
    (Path("logs/08.log"), {"message": "OK", "status": "OK"}),
]


def make_test(log_file, expected):
    def test(self):
        actual = xld_logchecker.parse_log(log_file)
        self.assertEqual(expected, actual)

    return test


TestLogchecker = type(
    "TestLogchecker",
    (unittest.TestCase,),
    {
        f"test_{log_file.stem}": make_test(log_file, expected)
        for log_file, expected in TESTS
    },
)


if __name__ == "__main__":
    unittest.main()
