#!/usr/bin/env python3
import argparse
import os
import stat
import shutil
import sys

if __name__ == '__main__':
    os.chmod('cp.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(
        description='cp python implementation.'
                    ' *NOTE*: like the original `cp`,'
                    ' if destination file is already exists, it will be overwritten.')
    parser.add_argument('source', nargs='+', type=str)
    parser.add_argument('destination', type=str)
    parser.add_argument('-r', required=False, action='store_true')

    args = parser.parse_args()
    src = args.source
    dest = args.destination
    if not os.path.isdir(dest):
        sys.stderr.write(f'target "{dest}" is not a directory\n')
    else:
        for item in src:
            try:
                shutil.copy2(item, dest)
            except IsADirectoryError:
                if args.r:
                    # If src item is directory, recursively copy all the files
                    # from src directory into directory named as basename of src located in destination directory
                    shutil.copytree(item, (os.path.join(dest, os.path.basename(item))), dirs_exist_ok=True)
                else:
                    sys.stderr.write(f'-r not specified; omitting directory "{item}"\n')
