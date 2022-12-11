#!/usr/bin/env python3
import os
import stat
import sys
import argparse


def wc(text):
    l = text.count('\n')
    w = len(text.split())
    c = len(text.encode('utf-8'))
    flags = [args.l, args.w, args.c]
    result = []
    if not any(flags):
        return [l, w, c]
    if args.l:
        result.append(l)
    if args.w:
        result.append(w)
    if args.c:
        result.append(c)
    return result


if __name__ == '__main__':
    # I assume it is not correct to overwrite permissions, but it shouldn't break anything (?)
    os.chmod('wc.py', stat.S_IRWXU)
    # Init argparse
    parser = argparse.ArgumentParser(description='wc python implementation', allow_abbrev=True)
    parser.add_argument('-l', required=False, action='store_true')
    parser.add_argument('-w', required=False, action='store_true')
    parser.add_argument('-c', required=False, action='store_true')
    parser.add_argument('input', nargs='*', default=sys.stdin, type=argparse.FileType('r'))
    args = parser.parse_args()
    total = ''
    try:
        text = args.input.read()
        print(' ', *wc(text))
    except AttributeError:
        for file in args.input:
            text = file.read()
            print(*wc(text), file.name)
            total += text
    if type(args.input) is list and len(args.input) > 1:
        print(*wc(total), 'total')
