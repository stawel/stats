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
parser.add_argument("-a", "--add-all", help="add to bits all possible values", action="store_true")
parser.add_argument("-d", "--delete", help="delete first  n bits", type=int, default=0)
parser.add_argument("-i", "--invert", help="invert bits", action="store_true")
parser.add_argument("-n", "--no-spaces", help="no spaces", action="store_true")
parser.add_argument("type", help="codding type", choices=['base64', 'base58', 'a7', 'a8', 'bac1', 'bac2', 'bac2x6', 'hex', 'oct', 'dec', 'bin', 'all', 'all-text','notes', 'notes2','base58b'])
args = parser.parse_args()
#print 'pawel'
#print args
#print args.square**2




def base64(x,l):
    return b64[x]

def base58(x,l):
    return b58[x]

def base58b(x,l):
    return b58b[x]


def bac1(x,l):
    return ba1[x]

def bac2(x,l):
    return ba2[x]

def bac2x6(x,l):
    return ba26[x]


def a7bit(x,l):
    return chr(x)#.decode("cp437")

def a8bit(x,l):
    return chr(x)#.decode("cp437")

def hexa(x,l):
    return ("{0:02x}").format(x)


def octa(x,l):
    return ("{0:02o}").format(x)

def deci(x,l):
    return ("{0:3d}").format(x)

def bina(x,l):
    return ("{0:0"+str(l)+"b}").format(x)

def notes(x,l):
    return nts[x]
def notes2(x,l):
    return nts2[x]


b58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz_______________________________'
b58b= '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/_________________________'
b64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/_________________________'
ba1 = "ABCDEFGHIKLMNOPQRSTUWXYZ_______________________________________________________"; 
ba2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_______________________________________________________"; 
ba26= "ABCDEFGHIJKLMNOPQRSTUVWXYZ______abcdefghijklmnopqrstuvwxyz_________________________________________________";
nts = "CDEFGAB_"
nts2= "ABCDEFG_"

#      1234567890123456789012345678901234567890123456789012345678901234

info = {'base64': (6,'t', base64), 'base58': (6,'t', base58), 'a7': (7,'t', a7bit), 'a8': (8,'t',a8bit), 'bac1': (5,'t', bac1), 'bac2': (5,'t', bac2)
, 'bac2x6': (6,'t', bac2x6), 'hex': (8,'d',hexa), 'oct': (6,'d',octa), 'dec':  (8,'d', deci), 'bin': (8,'d', bina)
, 'notes': (3,'n',notes), 'notes2': (3,'n',notes2), 'base58b': (6,'t',base58b)}

def splitString(s, size):
    return [s[i:i+size] for i  in range(0, len(s), size)]

def method2(method, x, l):
    if x<0: return '_'
    try:
        return method(x,l)
    except:
        return '_'

def convert(line, method, zeros, add=0):
    line = '0'*zeros + line
    l = info[method][0]
    if args.bits:
        l = args.bits
    s = splitString(line, l)
    if args.verbose: print s
    method = info[method][2]
    return [method2(method,int(x,2)+add, l) for x in s]


def xorString(s,x):
    l = len(x)
    r = []
    for i in range(0,len(s)):
        w = s[i]
        if x[i%l] == s[i]: w = '0'
        else: w= '1'
        r.append(w)
    return "".join(r)

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

    if args.invert:
        line = xorString(line, '1')


    line = line[args.delete:]

    if args.reverse:
        line = line[::-1]


    line = (line*args.jump)[args.start::args.jump]

    line = '0'*args.zeros + line

    if args.xor:
        line = xorString(line, args.xor)

    zeros = range(0,1)
    methods = [args.type]
    if args.type == 'all':
        methods = info.keys()
        print_all = True
    if args.type == 'all-text':
        methods = [ x for x in info.keys() if info[x][1]  == 't' ]
        print_all = True

    if print_all or args.verbose:
        print line

    adds = [0]
    if args.add_all:
        adds = range(-63,63)

    for m in methods:
        if print_all:
            print m
        if args.all_lengths:
            zeros = range(0, info[m][0])
        for a in adds:
            for z in zeros:
                c = convert(line, m, z, a)
                if args.no_spaces:
                    print "".join(c)
                else:
                    for x in c:
                        print x,
                    print



