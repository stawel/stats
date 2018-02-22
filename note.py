#!/usr/bin/python

from numpy import array
import sys



import argparse
parser = argparse.ArgumentParser()
parser.add_argument("notes", help="notes")
args = parser.parse_args()




d = {
'B': '[pkhb]',
'A': '[om]',
'G': '[lic]',
'F': '[wvsf]',
'E': '[te]',
'D': '[yxrnjg]',
'C': '[zuqda]'
}


print "".join([d[x] for x in args.notes])
