#!/usr/bin/python

from numpy import array
import sys
import itertools



import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("notes", help="notes")
parser.add_argument("-g", "--group", help="group letters", type=int, default=2)
parser.add_argument("-c", "--complete", help="complete to n letters", type=int, default=0)
args = parser.parse_args()




d1 = {
'_': '111',
'B': '110',
'A': '101',
'G': '100',
'F': '11',
'E': '10',
'D': '01',
'C': '00',
}

d2 = {
'_': '111',
'G': '110',
'F': '101',
'E': '100',
'D': '11',
'C': '10',
'B': '01',
'A': '00',
}


n = args.group


def dec(x,d, rev):
    if rev:
        x = x[::-1]
    w = [d[i] for i in x]
    s = "".join(w)
    return '0'*(args.complete-len(s))+s


def decode(l,d, rev = False):
    w = []
    inv = False
    for i in range(0,len(l)):
        x = dec(l[i],d,rev)
        w.append(x)

    return " ".join(w)


for line in sys.stdin:
    line = line.strip().replace(" ", "") 
    if len(line) <1:
        continue

    l1 = [line[i:i+n] for i in range(0, len(line), n)]

    print '#',line
    print decode(l1,d1)
    print decode(l1,d2)
    print decode(l1,d1,True)
    print decode(l1,d2,True)
