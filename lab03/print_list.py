#!/usr/bin/python

from sys import stdin

list = []

print ("Enter names to add to list. Ctl + D to end input.")

names = sys.stdin.readlines()

for x in names :
	list.append(x.rstrip('\n'))

print(list)
