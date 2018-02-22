#!/usr/bin/python

from numpy import array
import sys

verbose = False
print sys.argv
if sys.argv[-1] == '-v': verbose = True
stats = []
l = 0

def pr(a):
    o,i = a
    return i/float(o+i)

def pr2(a):
    o,i = a
    return o+i

def cut(line, how, ch):
    l = list(line)
    s = min(len(line), len(how));
#    print how
    for i in range(0,s):
        if how[i] != ch:
            l[i]=' ';
    return "".join(l)

def print_stats(m):
    m = m.replace(" ", "")
    if len(m) <2:
        return
    w = [m.count('0'), m.count('1')]
    stats.append(w)
    if verbose: print w,
    print pr(w)


for line in sys.stdin:
    m = line
    if len(sys.argv) > 2:
        m = cut(line, sys.argv[1], sys.argv[2])
    if verbose: print m,
    print_stats(m)




avr = sum(array(stats))/float(len(stats))

print avr, pr(avr), pr2(avr)
