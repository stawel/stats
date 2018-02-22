#!/usr/bin/python

from numpy import array
import sys
import random



import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()




d = "CDEFGAB"

w = [random.choice(d) for i in range(0,174)]
print "".join(w)
