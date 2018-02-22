#!/usr/bin/python

from numpy import array
import sys



import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("notes", help="notes")
args = parser.parse_args()


d1 = {
'B': 'pkhb',
'A': 'om',
'G': 'lic',
'F': 'wvsf',
'E': 'te',
'D': 'yxrnjg',
'C': 'zuqda'
}

d2 = {
'B': 'bhkp',
'A': 'mo',
'G': 'cil',
'F': 'fsvw',
'E': 'et',
'D': 'gjnrxy',
'C': 'adquz',
'_': ''
}


nt1 = {
'C': 0,
'D': 1,
'E': 2,
'F': 3,
'G': 4,
'A': 5,
'B': 6,
'_': 10,
}

nt2 = {
'A': 0,
'B': 1,
'C': 2,
'D': 3,
'E': 4,
'F': 5,
'G': 6,
'_': 10,
}

def decode(l2, nt,d, wrap = True):
    w = []
    for i in l2:
        if len(i) <2: continue
        y = nt[i[1]]
        x = d[i[0]]
#        print 'piotr:',x,y, ' aaa ', len(x),y
        if wrap:
            c = x[y%len(x)]
        else:
            if len(x)<=y:
                c = "'"+i+"'"
            else:
#            print 'piotr2:' , x,y
                c = x[y]
        w.append(c)
    return "".join(w)

for line in sys.stdin:
    line = ''+line.strip().replace(" ", "")+''
    if len(line) <1:
        continue

    n = 2
    l2 = [line[i:i+n] for i in range(0, len(line), n)]

#    print decode(l2,nt1,d1)
#    print decode(l2,nt2,d1)
#    print decode(l2,nt1,d2)
#    print decode(l2,nt2,d2)

#    print decode(l2,nt1,d1, False)
#    print decode(l2,nt2,d1, False)
    print decode(l2,nt1,d2, False)
    print decode(l2,nt2,d2, False)
