#!/usr/bin/python

import sys
from collections import Counter

data = [x.strip() for x in sys.stdin.readlines() if len(x.strip())>0 ]

for i in data:
    print sorted(Counter(i).items())

