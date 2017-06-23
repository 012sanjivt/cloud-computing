#!/usr/bin/env python

import sys

for line in sys.stdin:
    val = line.strip()
    vals = val.split(',')
    print "%s:%s:%s\t%s" % (vals[0], vals[1], vals[2], vals[3])
