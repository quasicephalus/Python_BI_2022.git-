#!/usr/bin/env python3
import argparse
import os
import stat
import sys

if __name__ == '__main__':
    os.chmod('rm.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(description='rm python implementation')
    parser.add_argument('-r', required=False, action='store_true')
    parser.add_argument('path', nargs='+', type=str)
    args = parser.parse_args()
    path = args.path
    for file in path:
        try:
            os.remove(file)
        except IsADirectoryError:
            if args.r:
                os.rmdir(file)
            else:
                sys.stderr.write(f'cannot remove "{file}": Is a directory\n')
