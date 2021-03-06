#!/usr/bin/python

import sys

# Check command line arguments and open input file
if (len(sys.argv) != 2) :
	print("Usage: %s <input_file>" % sys.argv[0])

f = open(sys.argv[1], 'r')

dict = {}

print ("ADDING EMPLOYEE DETAILS:")

# Read input from file and store in nested dictionaries
while True :
	line = f.readline().strip()
	if line == '' :
		break
	id = int(line)
	print ("\tAdding employee ID %d" % id)
	name = f.readline().strip()
	salary = int(f.readline().strip())
	start = f.readline().strip()
	
	temp = { 'id' : id, 'name' : name, 'salary' : salary, 'start' : start }
	dict[id] = temp

print "EMPLOYEE DETAILS SAVED\n"

# Function to find and display employee information based on ID
def find_emp (id) :
	print("ID:\t\t%d" %  id)
	print("Name:\t\t%s" % dict[id]['name'])
	print("Salary:\t\t%d" % dict[id]['salary'])
	print("Start Date:\t%s" % dict[id]['start'])
	print ""
	user_input()

# Function to accept user input
def user_input () :
	sys.stdout.write("Enter employee ID to search: ")
	find_emp(int(raw_input().strip()))

# Call user input function
user_input()

