pangram
=======

[![Build Status](https://travis-ci.org/hugovk/pangram.svg?branch=master)](https://travis-ci.org/hugovk/pangram)

Find the shortest pangrammatic window in a text file.

Examples:

```
pangram.py file.txt
pangram.py dir/*.txt
pangram.py dir_with_subdirs/*.txt
```

Usage:

```
usage: pangram.py [-h] [-t TEXT] [inspec [inspec ...]]

Find the shortest pangrammatic window in a text file.

positional arguments:
  inspec                Input file spec (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Check this text instead of a file (default: None)
```

