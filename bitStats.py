#!/usr/bin/python

from numpy import array
import sys

class bcolors:
    MAX = '\033[32m'
    MIN = '\033[33m'
    ENDC = '\033[0m'

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="verbose", action="store_true")
parser.add_argument("-g", "--group", help="group n bits", type=int, default=0)
parser.add_argument("-m", "--max-range", help="max group range", type=int, default=8)
args = parser.parse_args()

def splitString(s, size):
    return [s[i:i+size] for i  in range(0, len(s), size)]

def stats(l, n):
    w = []
    for i in range(0,n):
        b0=l[i::n].count('0')
        b1=l[i::n].count('1')
        if b0+b1<=0: b0+=1
        w.append(float(b1)/(b0+b1))
    return w

def format_stats(s, c_min=False, c_max=False):
    mi = s.index(min(s))
    ma = s.index(max(s))
    w = []
    for i in range(0,len(s)):
        f = "%.2f"%s[i]
        if c_min and i == mi: f = bcolors.MIN+f+bcolors.ENDC
        if c_max and i == ma: f = bcolors.MAX+f+bcolors.ENDC
        w.append(f)
    return w

for line in sys.stdin:
    line = line.strip().replace(" ", "")
    if len(line) <1 or line[0]=='#':
        print line
        continue

    if args.group > 0:
        s = stats(line, args.group)
        print " ".join(format_stats(s, True, True)), line
        continue

    min_range = 2
    mi = [min(stats(line, n)) for n in range(min_range,args.max_range+1)]
    ma = [max(stats(line, n)) for n in range(min_range,args.max_range+1)]
    w1 = format_stats(mi,c_min=True)
    w2 = format_stats(ma,c_max=True)
    print " ".join([str(i+min_range)+':'+x+'/'+y for (i,x,y) in zip(range(0,len(w1)),w1,w2)]), line
