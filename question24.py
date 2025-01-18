"""
24.	Write a Python program to add an item to a tuple.
"""

tuple1 = tuple(input("enter the elements (comma separated): ").split(","))
value = input("enter the value to be added:")

updated_tuple = tuple1 + (value,)
print("updated tuple:", updated_tuple)

