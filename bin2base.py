#!/usr/bin/python

from numpy import array
import sys

#reload(sys)
#sys.setdefaultencoding('cp437')


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="verbose", action="store_true")
parser.add_argument("-z", "--zeros", help="add zeros at the begining", type=int, default=0)
parser.add_argument("-l", "--all-lengths", help="add all possible zeros at the begining", action="store_true")
parser.add_argument("-r", "--reverse", help="reverse bitstream", action="store_true")
parser.add_argument("-x", "--xor", help="xor bitstream")
parser.add_argument("-j", "--jump", help="jump bits", type=int, default=1)
parser.add_argument("-b", "--bits", help="group in bits", type=int)
parser.add_argument("-s", "--start", help="start at bit", type=int, default=0)
parser.add_argument("-d", "--delete", help="delete first  n bits", type=int, default=0)
parser.add_argument("-i", "--invert", help="invert bits", action="store_true")
parser.add_argument("-n", "--no-spaces", help="no spaces", action="store_true")
parser.add_argument("base", help="base", type=int)
args = parser.parse_args()
#print 'pawel'
#print args
#print args.square**2



base= '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/_________________________'



print_all = False


for line in sys.stdin:
    line = line.strip().replace(" ", "")
    line = line.strip().replace("|", "")
    line = line.strip().replace("^", "")
    if len(line) <1:
        print ""
        continue
    if line[0]=='#':
        print line
        continue


    if args.reverse:
        line = line[::-1]

    x = int(line, 2)
    n = args.base
#    print x, n
    w = []
    while x>0:
        w.append(x%n)
        x/=n
    print "".join([base[i] for i in w][::-1])

