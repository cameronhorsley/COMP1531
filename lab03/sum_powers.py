#!/usr/bin/python

import sys

if (len(sys.argv) != 2) :
	print("Usage: %s <integer>" % sys.argv[0])
	sys.exit(1)

	
n = int(sys.argv[1])
sum = n;
sys.stdout.write ("%d " %n)


for x in range (2, n+1) :
	temp = n;
	for power in range(1, x) :
		temp = temp*n
		
	sys.stdout.write("+ %d^%d " %(n, x))
	sum = sum + temp
	
sys.stdout.write("= %d" %sum)
print ""
