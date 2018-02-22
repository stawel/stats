#!/usr/bin/python

import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--group", help="group letters", type=int, default=1)
parser.add_argument("-s", "--string", help="string to add", default="\n")
args = parser.parse_args()



lines = []

for line in sys.stdin:
    line = line.strip().replace(" ", "")
    if len(line) <1:
        continue

    lines.append(line)



n = args.group


for l in lines:
    l2 = [l[i:i+n] for i in range(0, len(l), n)]
    if len(l2[-1]) != len(l2[0]):
        l2 = l2[:-1]
    print args.string.join(l2)