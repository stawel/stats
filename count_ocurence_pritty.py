#!/usr/bin/python

import sys
from collections import Counter
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="verbose", action="store_true")
parser.add_argument("-g", "--group", help="group letters", type=int, default=1)
args = parser.parse_args()



lines = []

for line in sys.stdin:
    line = line.strip().replace(" ", "")
    if len(line) <1:
        continue

    lines.append(line)



n = args.group

result = []
rc = Counter()
for l in lines:
    l2 = [l[i:i+n] for i in range(0, len(l), n)]
    c = Counter(l2)
    result.append(c)
    rc+=c
#    print len(c), c , l

for i in rc:
    print i+':',rc[i],'\t',
    for j in result:
        print j[i],
    print 