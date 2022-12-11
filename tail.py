#!/usr/bin/env python3

import sys
import argparse
import os
import stat


def tail(lines, n):
    return lines[len(lines) - n:len(lines)]


if __name__ == '__main__':
    os.chmod('tail.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(description='tail python implementation')
    parser.add_argument('input', nargs='*', default=sys.stdin, type=argparse.FileType('r'))
    parser.add_argument('-n', default=10, type=int)
    args = parser.parse_args()
    n = args.n
    try:
        lines = args.input.readlines()
        print(*tail(lines, n), sep='', end='')
    except AttributeError:
        lines = []
        for i, file in enumerate(args.input):
            lines += file.readlines()
            if len(args.input) > 1:
                print(f'==> {file.name} <==')
            print(*tail(lines, n), sep='', end='')
            # Any advice about optimal solution for \n's between files will be appreciated
            if i != len(args.input) - 1:
                print()
