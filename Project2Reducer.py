#!/usr/bin/env python

from operator import itemgetter
import sys

matrixIndexA = list() 		
matrixValueA = list() 
matrixIndexB = list() 		
matrixValueB = list()
currKey = None
rowA = int(sys.argv[1])
colA = int(sys.argv[2])
rowB = int(sys.argv[3])
colB = int(sys.argv[4])
	

for line in sys.stdin:
	(key, val) = line.strip().split('\t')
    
    	compKey = key.split(':')
	matrixName=compKey[0]
    	if currKey == matrixName or currKey == None:
    		matrixIndexA.append(compKey[1]+compKey[2])
    		matrixValueA.append(float(val))
		currKey= matrixName
	else:
		matrixIndexB.append(compKey[1]+compKey[2])
    		matrixValueB.append(float(val))	


if colA==rowB:
	for i in range(0, rowA):
		for j in range(0, colB):
			sum = 0;
			for k in range(0, rowB):
				if str(i)+str(k) in matrixIndexA:
					x= matrixValueA[matrixIndexA.index(str(i)+str(k))]
				else:
					x= 0
				if str(k)+str(j) in matrixIndexB:
					y= matrixValueB[matrixIndexB.index(str(k)+str(j))]
				else:
					y= 0
				sum+= x * y
			print "%s, %s, %.2f" % (i,j,sum)
			

else:
	print("This matrix multiplication is not possible as ColA is not equal to RowB.")





    
	