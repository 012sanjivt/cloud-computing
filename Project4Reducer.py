#!/usr/bin/env python

from operator import itemgetter
import sys

current_key = None
current_count = 0
key = None
dataDict1 = {}
dataDict2 = {}

for line in sys.stdin:
    line = line.strip()
    (key, count) = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_key == key:
        current_count += count
    else:
        if current_key:
		if len(current_key) == 10:
			dataDict1[current_key] = current_count
		else:
			dataDict2[current_key] = current_count
        current_count = count
        current_key = key
if current_key == key:
	if len(current_key) == 10:
		dataDict1[current_key] = current_count
	else:
		dataDict2[current_key] = current_count
print('\n\nTop 10 10-mers...')
counter =0
for key, value in sorted(dataDict1.iteritems(), key =lambda (k,v) : (v,k), reverse=True):
	if counter<10:	
		print '%s\t%s' % (key, value)
		counter+=1
print('\nTop 10 20-mers...')
counter = 0
for key, value in sorted(dataDict2.iteritems(), key =lambda (k,v) : (v,k), reverse=True):
	if counter<10:	
		print '%s\t%s' % (key, value)
		counter+=1
		





    
