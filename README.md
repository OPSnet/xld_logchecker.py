# XLD Logchecker

![Travis-CI Status](https://img.shields.io/travis/com/OPSnet/xld_logchecker.py/master.svg) 
![PyPI](https://img.shields.io/pypi/v/xld_logchecker.svg)

This is a fork of https://github.com/puddly/xld_logsigner, to be used within our 
downstream applications, removing unnecessary functionality that we do not need. 

Based heavily on [barrybingo/xld_sign](https://github.com/barrybingo/xld_sign).
This is a complete disassembly of the XLD log signing algorithm, re-implemented in
Python 3.5+.

# Usage

    usage: xld.py [-h] (--verify | --sign) FILE

    Verifies and resigns XLD logs

    positional arguments:
      FILE        path to the log file

    optional arguments:
      -h, --help  show this help message and exit
      --verify    verify a log
      --sign      sign or fix an existing log

# Overview

The final code isn't pretty, but it is simple enough to describe the algorithm.

 1. The log is encoded as UTF-8 and hashed with a SHA-256 variant that uses a different IV.
 2. The digest is converted to hex and the string `\nVersion=0001` is appended onto the end.
 3. The versioned hex-digest is then passed through an unidentified scrambling function that operates on pairs of bytes (open an issue if you recognize it).
 4. The resulting bytestring is then encoded using a 65-character lookup table with a strange mapping.
