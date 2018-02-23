#!/usr/bin/python

from numpy import array
import sys



import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--remove-spaces", help="remove spaces", action="store_true")
parser.add_argument("-u", "--to-upper", help="to upper case", action="store_true")
parser.add_argument("-l", "--to-lower", help="to lower case", action="store_true")
parser.add_argument("-o", "--only-letters", help="only letters", action="store_true")
parser.add_argument("-v", "--verbose", help="verbose", action="store_true")
parser.add_argument("type", help="codding type", choices=['base64', 'base58', 'a7', 'a8', 'bac1', 'bac2', 'notes','notes2', 'hex','oct'])
args = parser.parse_args()
#print 'pawel'
#print args
#print args.square**2



def clean(line):
    if args.remove_spaces:
        line = line.replace(" ", "");
    if args.only_letters:
        line = ''.join(x for x in line if x.isalpha())
    if args.to_upper:
        line = line.upper()
    if args.to_lower:
        line = line.lower()
    return line


b58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz_______________________________'
b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/_________________________'
ba1 = "ABCDEFGHIKLMNOPQRSTUWXYZ_______________________________________________________"; 
ba2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_______________________________________________________"; 
nts1= "CDEFGABH_______________________________________________________"; 
nts2= "ABCDEFGH_______________________________________________________"; 
hx  = "0123456789ABCDEF_______________________________________________________"; 
oc  = "01234567_______________________________________________________"; 
#      12345678901234567890123456


def ret(i, x , bits):
    if i>=0:
        return ("{0:0"+str(bits)+"b}").format(i)
    else:
        if args.verbose:
            print "ERROR:", x
        return ""

def myindex(b, x):
    try:
        i = b.index(x)
    except ValueError:
        i = -1
    return i

def base64(x):
    return ret(myindex(b64, x),x,6)

def base58(x):
    return ret(myindex(b58,x),x,6)

def bac1(x):
    return ret(myindex(ba1,x.upper()),x,5)

def bac2(x):
    return ret(myindex(ba2,x.upper()),x,5)


def a7(x):
    return ret(ord(x), x, 7)

def a8(x):
    return ret(ord(x), x, 8)

def notes(x):
    return ret(myindex(nts1,x.upper()),x,3)

def notes2(x):
    return ret(myindex(nts2,x.upper()),x,3)

def hex(x):
    return ret(myindex(hx,x.upper()),x,4)

def oct(x):
    return ret(myindex(oc,x),x,3)



def convert(line):
    method = globals()[args.type]
    return [method(x) for x in line]

for line in sys.stdin:
    line = clean(line.strip())
    if args.verbose:
        print line
    c = convert(line)
    for x in c:
        print x,
    print



