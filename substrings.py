#!/usr/bin/python

from numpy import array
import sys



import argparse
parser = argparse.ArgumentParser()
parser.add_argument("string", help="string")
parser.add_argument("-r", "--reverse", help="reverse string", action="store_true")
parser.add_argument("-m", "--minimum", help="minimum substring length", type=int, default=0)
args = parser.parse_args()


def findSubStrings(s, x):
    w = []
    for i in range(0,len(x)):
        for j in range(len(x)-1,i,-1):
            if s.find(x[i:j]) >= 0:
                if len(x[i:j]) >= args.minimum:
                    w.append(x[i:j])
                break

    return w


x =  args.string
if args.reverse:
    x = args.string[::-1]

for line in sys.stdin:
    line = line.strip().replace(" ", "")
    if len(line) <1:
        continue
    if line == x:
        print line+':', x
        continue


    w = findSubStrings(line, x)
    w.sort(key=len, reverse=True)

    print line+':', " ".join(w)
