#!/usr/bin/env python

import sys
valueList = list()
skipCnt = 0
genome = ''
for line in sys.stdin:
	if skipCnt > 0:
		val = line.strip()
		genome= genome +val
	else:
		skipCnt = 1	
valueList= list(genome)
window1 = 10
comp1 = len(valueList) - window1 + 1
for i  in range(0, comp1):
	str1 = ''.join(valueList[i:i+window1])
	print "%s\t%s" % (str1,1)

window2= 20
comp2 = len(valueList) - window2 + 1
for i  in range(0, comp2):
	str2 = ''.join(valueList[i:i+window2])
	print "%s\t%s" % (str2,1)
	
	
