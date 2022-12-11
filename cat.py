#!/usr/bin/env python3

import sys
import argparse
import os
import stat

if __name__ == '__main__':
    os.chmod('cat.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(description='cat python implementation')
    parser.add_argument('input', nargs='*', default=sys.stdin, type=argparse.FileType('r'))
    args = parser.parse_args()
    try:
        cat = args.input.read()
        print(cat)
    except AttributeError:
        cat = ''
        for file in args.input:
            cat += file.read()
        print(cat, end='')
