#!/usr/bin/python

from numpy import array
import sys
import itertools



import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("notes", help="notes")
parser.add_argument("-g", "--group", help="group letters", type=int, default=2)
parser.add_argument("-c", "--complete", help="complete to n letters", type=int, default=6)
args = parser.parse_args()




d1 = {
'_': '111',
'B': '110',
'A': '101',
'G': '100',
'F': '011',
'E': '010',
'D': '001',
'C': '000',
}

d2 = {
'_': '111',
'G': '110',
'F': '101',
'E': '100',
'D': '011',
'C': '010',
'B': '001',
'A': '000',
}



n = args.group


def dec(x,d, rev = False):
    if rev:
        x = x[::-1]
    w = 0
    for i in x:
        w*=7;
        w+=int(d[i],2)
    w= ("{0:0" +str(args.complete)+"b}").format(w)
    return w[-args.complete:]

def decode(l,d, rev = False):
    w = []
    inv = False
    for i in range(0,len(l)):
        x = dec(l[i],d, rev)
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
    print decode(l1,d1, True)
    print decode(l1,d2, True)
