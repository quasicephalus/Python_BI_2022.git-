#!/usr/bin/env python3
import argparse
import os
import stat


def ls(path):
    if os.path.isdir(path):
        listdir = os.listdir(path)
        return sorted(listdir, key=lambda item: item.strip('.'))
    return [path]


if __name__ == '__main__':
    os.chmod('ls.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(description='ls python implementation')
    parser.add_argument('-a', required=False, action='store_true')
    parser.add_argument('path', nargs='*', default=os.getcwd(), type=str)
    args = parser.parse_args()
    # If -a then add strange dots
    # TypeError rises when we pass > 1 dirs
    if args.a:
        try:
            print('.', '..', *ls(args.path))
        except TypeError:
            for path in args.path:
                if len(args.path) > 1:
                    print(path, ':', sep='')
                print('.', '..', *ls(path))
    # Else filter items not starting with dot
    else:
        try:
            nodot = filter(lambda x: not x.startswith('.'), ls(args.path))
            print(*nodot)
        except TypeError:
            for path in args.path:
                nodot = filter(lambda x: not x.startswith('.'), ls(path))
                if len(args.path) > 1:
                    print(path, ':', sep='')
                print(*nodot)
