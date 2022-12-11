#!/usr/bin/env python3
import argparse
import os
import stat
import sys

if __name__ == '__main__':
    os.chmod('mkdir.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(description='mkdir python implementation')
    parser.add_argument('-p', required=False, action='store_true')
    parser.add_argument('path', nargs='+', type=str)
    args = parser.parse_args()
    path = args.path
    for dir in path:
        try:
            os.mkdir(dir)
        except FileNotFoundError:
            if args.p:
                os.makedirs(dir)
            else:
                sys.stderr.write(f'Cannot create directory "{dir}": No such file or directory\n')
        except FileExistsError:
            if args.p:
                os.makedirs(dir, exist_ok=True)
            else:
                sys.stderr.write(f'Cannot create directory "{dir}": File exists\n')
