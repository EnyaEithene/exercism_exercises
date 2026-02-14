"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2
SUPERLIST = 3
EQUAL = 1
UNEQUAL = 4

def is_sublist(small, big):
    if not small:
        return True
    
    for i in range(len(big) - len(small) + 1):
        if big[i:i+len(small)] == small:
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return 1
    if is_sublist(list_one,list_two):
        return 2
    if is_sublist(list_two,list_one):
        return 3
    return 4