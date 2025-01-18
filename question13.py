"""
13.	Write a  Python program to multiply all the items in a list
"""

def multiply_list(value_list):
    result = 1
    for i in value_list:
        result *= i
    print ("product of the list items = ", result)

value = [1,2,3,4,5,6,-1]
multiply_list(value)