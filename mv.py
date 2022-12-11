#!/usr/bin/env python3
import argparse
import os
import stat
import shutil

if __name__ == '__main__':
    os.chmod('mv.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(
        description='mv python implementation. '
                    '*NOTE*: like the original `mv`,'
                    ' if destination file is already exists, it will be lost.'
    )
    parser.add_argument('source', nargs='+',type=str)
    parser.add_argument('destination', type=str)

    args = parser.parse_args()
    source = args.source
    dest = args.destination

    for src in source:
        try:
            shutil.move(src, dest)
        except FileNotFoundError:
            print(f'Cannot stat "{src}": No such file or directory')
        # This one occurs when destination contains src file, but original `mv` can handle it, so mine should as well
        except shutil.Error:
            file = os.path.basename(src)
            try:
                os.remove(os.path.join(dest, file))
                shutil.move(src, dest)
            except IsADirectoryError:
                print(f'mv: cannot move "{src}" to "{dest}": Directory not empty')
        # And this one when destination is directory named the same as src
        except FileExistsError:
            print(f'Cannot overwrite non-directory "{dest}" with directory "{src}"')


