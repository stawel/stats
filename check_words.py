#!/usr/bin/python

import sys
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--minimum", help="minimum characters", type=int, default=0)
parser.add_argument("-q", "--quiet", help="dont print input string", action="store_true")
parser.add_argument("-l", "--longest", help="check longest word", action="store_true")
parser.add_argument("-b", "--begin", help="check longest word from begining", action="store_true")
parser.add_argument("-f", "--farest", help="check longest words from begining", action="store_true")
parser.add_argument("-d", "--dictionary", help="use dictionary", default="")
parser.add_argument("-a", "--add-words", help="add 2 letter words", action="store_true")
parser.add_argument("-w", "--word", help="minimum charactersper word", type=int, default=2)
args = parser.parse_args()
#print 'pawel'
#print args
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))



dict_tree = {}

def add(root, s):
    if len(s) == 0:
        root['$'] = {}
    else:
        k = s[0]
        if k not in root:
            root[k] = {}
        add(root[k], s[1:])


with open(os.path.join(__location__,"words.txt"+args.dictionary)) as word_file:
    english_words = [word.strip().upper() for word in word_file]

    for w in english_words:
        if len(w)>=args.word:
            add(dict_tree, w)


english_words2 = ['of','to','in','is','on','by','it','or','be','at','as','an','we','us','if','my',
'do','no','he','up','so','pm','am','me','re','go',
'I','a', 'Im', 'xor', 'id', 'via', 'viacoin', 'coin', 'bitcoin']


if args.add_words:
    for w in english_words2:
        add(dict_tree, w.strip().upper())



#print dict_tree

def find_word(root, line, i, n, w):
    if '$' in root: 
        w.append(i)
#        print '1'
#    print line[i], '-'
    if i>= n: return w
    k = line[i]
    if k in root:
        return find_word(root[k], line, i+1,n, w)
    return w


def mcount(f, i, n):
    if i>=n: return (0, [])
    pos = f[i]
    (co, wo) = mcount(f,i+1,n)
    for x in pos:
        c, w = mcount(f,x,n)
        if c + x-i > co:
            co = c + x-i
            wo = [(i,x)] + w
    return (co, wo)


#print find_word(dict_tree,"YOUWHO______",0,8,[]), "pawel"

#exit(1)

def countFarest(f,i,n):
    if i>=n: return [(0,i,i)]
    w = countFarest(f,i+1,n)
    pos = f[i]
    l = 0
    p = i
    for x in pos:

        l2 = x-i 
        l3 = l2 + w[l2-1][0]
#        print "$", i,l,l2,l3,x
#        print w
        if l3 > l:
            l = l3
            p = x
    return [(l,i,p)]+w

def printFarest(w,i,line):
    if len(w)<=i: return
    (l,a,p) = w[i]

#    print (l,i,p), i,p, line[i:p],
    print line[i:p],
    if l == 0: return
    printFarest(w,p,line)

def formatLine(l):
    d = [('0','O'), ('4','A'),('8','B'),('3','E'),('6','G'),('1','l'),('5','S'),('7','T'),('2','Z')]
    for (i,j) in d:
        l=l.replace(i,j)
    l=l.upper()
    return l

for line in sys.stdin:
    c = 0
    i = 0
    n = len(line)
    f = {}
    for i in range(0,n):
        f[i] = sorted(find_word(dict_tree, formatLine(line), i, n, []), reverse=True)

    if args.longest:
        l = 0
        p1 = 0
        p2 = 0
        if args.begin:
            r = [0]
        else:
            r = range(0,n)
        for i in r:
            if len(f[i]) > 0:
                l2 = f[i][0] - i
                if l2 > l:
                    p1 = i
                    p2 = f[i][0]
                    l = l2
        print l, line[p1:p2], line,
        continue

    if args.farest:
        w = countFarest(f,0,n)
#        print f
#        print w
        if args.begin:
            r = 0
        else:
            r = 0
            l = 0
            for i in range(0,n):
                if l < w[i][0]:
                    l = w[i][0]
                    r = i
        print w[r][0],
        printFarest(w,r,line)
        print line,
        continue

#    print f
    (c, w) = mcount(f,0,n)
#    print w
    if c >= args.minimum:
        print c, 
        for (i,j) in w:
            print line[i:j],
        if args.quiet: print ""
        else: print line,
