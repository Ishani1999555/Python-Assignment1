"""
25.	Write a Python program to convert a list to a tuple.
"""

list_value = input("enter the list elements (comma separated): ").split(",")
result = tuple(list_value)
print(f"the given list converted to a tuple : {result}")
