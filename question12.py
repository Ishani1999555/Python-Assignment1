"""
12.	Write a  Python program to sum all the items in a list. Using both loop and sum function.
"""
from question1 import result


def sumfunction_with_loop(value_list):
    result =0
    for i in value_list:
        result+= i
    print ("sum of the list items = ", result)

def sum_function(value_list):
    result = sum(value_list)
    print("sum of the list items(sum function) = ", result)

value = [1,2,3,4,5,6,-1]
sumfunction_with_loop(value)
sum_function(value)




