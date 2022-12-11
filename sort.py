#!/usr/bin/env python3

import sys
import argparse
import os
import stat

if __name__ == '__main__':
    os.chmod('sort.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(description='sort python implementation')
    parser.add_argument('input', nargs='*', default=sys.stdin, type=argparse.FileType('r'))
    args = parser.parse_args()
    try:
        lines = [line.strip() for line in args.input.readlines()]
        print(*sorted(lines), sep='\n')
    except AttributeError:
        lines = []
        for file in args.input:
            lines += [line.strip() for line in file.readlines()]
        print(*sorted(lines), sep='\n')
