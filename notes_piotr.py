#!/usr/bin/python

from numpy import array
import sys
import itertools



import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("notes", help="notes")
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
'B': '111',
'A': '110',
'G': '101',
'F': '100',
'E': '011',
'D': '010',
'C': '001',
'_': '000',
}


d3 = {
'_': '111',
'G': '110',
'F': '101',
'E': '100',
'D': '011',
'C': '010',
'B': '001',
'A': '000',
}
d4 = {
'G': '111',
'F': '110',
'E': '101',
'D': '100',
'C': '011',
'B': '010',
'A': '001',
'_': '000',
}

d5 = {
'F': '111',
'E': '110',
'D': '101',
'C': '100',
'B': '011',
'A': '010',
'_': '001',
'G': '000',
}

d6 = {
'F': '111',
'E': '110',
'D': '101',
'C': '100',
'B': '011',
'A': '010',
'G': '001',
'_': '000',
}



def xorString(s,x):
    l = len(x)
    r = []
    for i in range(0,len(s)):
        w = s[i]
        if x[i%l] == s[i]: w = '0'
        else: w= '1'
        r.append(w)
    return "".join(r)

n = 2


def dec(x,d):
#    x = x[::-1]
    return "".join([d[c] for c in x])


def decode(l,d,ea):
    w = []
    inv = False
    for i in range(0,len(l)):
        x = dec(l[i],d)
#        print '!!!!!!!!!!', x, l[i]
        if inv:
            x = xorString(x,'111111');
#            x = '111111'
            inv = False
        elif l[i] == ea:
            inv = True
            continue
        w.append(x)

    return " ".join(w)


def getD(p):
    l = ['A','B','C','D','E','F','G','_']
    d ={}
    for i,j in zip(l,p):
        d[i]=j
    return d


for line in sys.stdin:
    line = line.strip().replace(" ", "") 
    if len(line) <1:
        continue
    line2 = 'G'+line
    line3 = line[::-1]
    line4 = 'G'+line3

    l1 = [line[i:i+n] for i in range(0, len(line), n)]
    l2 = [line2[i:i+n] for i in range(0, len(line2), n)]
    l3 = [line3[i:i+n] for i in range(0, len(line3), n)]
    l4 = [line4[i:i+n] for i in range(0, len(line4), n)]

    print '#',line
    perm = list(itertools.permutations(['000', '001', '010', '011','100','101','110','111']))
    for l in [l1,l2,l3,l4]:
        for d in [d1,d2,d3,d4,d5,d6]:
#        for p in perm:
            for ea in ['EA_']:#,'_AE']:
#                d = getD(p)
            #print d
                print  decode(l,d, ea)
