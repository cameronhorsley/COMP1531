import random
import copy

"""
This function returns a new list that is created by shuffling the elements of the
provided list
:param li: The list to be shuffled
:return shuffled_list: The shuffled list
"""

user_list = input("Put a few comma separated characters\n").split(',')
#user_list = [1,2,3,4,5,6,7,8,9]
#user_list = ['ted','bill',4,9,103]

def shuffle(li):
    random.shuffle(li)
    return li

print(shuffle(user_list))
