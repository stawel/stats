#!/usr/bin/python

import sys



for line in sys.stdin:
    line = line.strip().replace(" ", "")
    if len(line) <1:
        continue

    print len(line), line
