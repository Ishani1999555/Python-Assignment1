"""
26.	Write a Python program to find the index of an item in a tuple.
"""

tuple_inp = tuple(input("enter the tuple elements (comma separated):").split(","))
value = input("enter an item: ")

if value in tuple_inp:
    value_index = tuple_inp.index(value)
    print(f"{value} is at index {value_index} in the tuple - {tuple_inp}")
else:
    print(f"{value} is not present in the tuple - {tuple_inp}")

