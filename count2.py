#!/usr/bin/python

import sys
from collections import Counter

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="verbose", action="store_true")
parser.add_argument("-s", "--short", help="short answer", action="store_true")
parser.add_argument("-g", "--group", help="group letters", type=int, default=2)
parser.add_argument("-j", "--jump", help="jump letters", type=int, default=1)
parser.add_argument("-p", "--procent", help="print procent", action="store_true")
args = parser.parse_args()

data = [x.strip() for x in sys.stdin.readlines() if len(x.strip())>0 ]

n = args.group

w = []
cnt = 0
for s in data:
    for i in range(0,len(s)-n+1, args.jump):
	w.append(s[i:i+n])
        cnt+=1
#print w

cw = Counter(w).items()

if args.short:
    w = 0
    for s,i in cw:
        if i > 1: 
            w+=i
#            print i
    print w
    exit(0)


cw.sort(key=lambda x: x[1])
for i,j in cw:
    if args.procent:
        print i,j*1.0/cnt
    else:
        print i,j
