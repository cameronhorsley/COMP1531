#!/usr/bin/python

import sys

print("Hello, git!")

#if (len(sys.argv) != 2):
#	print ("Usage: %s <integer>" % sys.argv[0])
#	sys.exit(1)
	
#n = int(sys.argv[1])

for x in range(1, 101) :
	if (x % 3 == 0 and x % 5 == 0) :
		print("FIZZ BUZZ")
	elif (x % 3 == 0) :
		print("FIZZ")
	elif (x % 5 == 0) :
		print("BUZZ")
	else :
		print(x)
