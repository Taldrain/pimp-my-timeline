#!/usr/bin/python2.7

import argparse
import datetime
import sys
import subprocess
import os

def parse_arg():
    parser = argparse.ArgumentParser(description="Pimp you github timeline")
    parser.add_argument('inputFile', help='the input file to draw')
    parser.add_argument('date', help='the date to begin')
    args = parser.parse_args()
    return args

def check_file(iF):
    with open(iF) as f:
        for i, l in enumerate(f):
            pass
    if (i + 1) != 7:
        sys.stderr.write("The file should have 7 lines\n")
        sys.exit(1)

def parse_file(iF, date):
    working_date = date
    with open(iF) as f:
        c = f.read(1)
        while c:
            if c == '\n':
                date += datetime.timedelta(days=1)
                working_date = date
            elif c == '#':
                strDate = working_date.strftime('%a %b %d 00:00 %Y')
                os.environ['GIT_COMMITTER_DATE'] = strDate
                subprocess.call(['git', 'commit', '--allow-empty', '--allow-empty-message', '-m ""', '--date="' + strDate + '"'])
                working_date += datetime.timedelta(days=7)
            else:
                working_date += datetime.timedelta(days=7)
            c = f.read(1)



def main():
    args = parse_arg()
    check_file(args.inputFile)
    date = datetime.datetime.strptime(args.date, '%Y-%m-%d')
    # necessary, probably due to time zone
    date += datetime.timedelta(days=1)
    parse_file(args.inputFile, date)


if __name__ == '__main__':
    main()
