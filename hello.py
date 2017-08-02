#!/usr/bin/python

import sys



def nfizz(n) :
	for x in range(1, n+1) :
		if (x % 3 == 0 and x % 5 == 0) :
			print("FIZZ BUZZ")
		elif (x % 3 == 0) :
			print("FIZZ")
		elif (x % 5 == 0) :
			print("BUZZ")
		else :
			print(x)

n = 100;

if (len(sys.argv) == 2):
	n = int(sys.argv[1])
nfizz(n)

