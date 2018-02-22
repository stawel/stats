#!/usr/bin/python

import sys


lines = []

for line in sys.stdin:
    line = line.strip().replace(" ", "")
    if len(line) <1:
        continue

    lines.append(line)

x = map(list, zip(*lines))
for i in x:
    print "".join(i)

