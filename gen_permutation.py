#!/usr/bin/python

from numpy import array
import sys



import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="verbose", action="store_true")
parser.add_argument("-j", "--join", help="join string", default="")
parser.add_argument("-z", "--zero", help="allow empty string", action="store_true")
args = parser.parse_args()



def genStreams(lines):
    if len(lines) == 0: return [[]]
#    print lines
    w = []
    for i in range(0,len(lines)):
        a = lines[:i]
        l = lines[i]
        b = lines[i+1:]

        g = genStreams(a+b)
        w+= [ [l] + x for x in g]
        if args.zero:
            w+=g
    return w



lines = []

for line in sys.stdin:
    line = line.strip().replace(" ", "")
    if len(line) <1:
        continue

    lines.append(line)


g = genStreams(lines)


for i in g:
    print args.join.join(i)

