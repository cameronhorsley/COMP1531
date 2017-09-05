'''
Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and 
sorting them alphanumerically. Suppose the following input is 
supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Your program should take in only one line of input.

You may assume that your program will only be tested
with valid inputs.
'''

# sentence = input()
# sentence = "Hello world and practice makes perfect and Hello world again"
# sentence = "one two three One tWo thREE one"
# sentence = "hello Hello There there am I"
sentence = "Hello hello There there am I"


# Define this function to return the expected output
# Do not print it from this function
def singlify(s):
    words = s.split()
    temp = []
    to_print = []
    
    for word in words:
    	if word.lower() in temp:
    		continue
    	else: 
    		to_print.append(word)
    		temp.append(word.lower())
    
    to_print.sort(key=lambda x: x.lower())
    print(' '.join(to_print))
    
singlify(sentence)
