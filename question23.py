"""
23.	Write a Python program to unpack a tuple into several variables.
"""

tuple_values = tuple(input("Enter the values (comma separated): ").split(","))
value1, *value2, value3 = tuple_values
print(f"tuple value 1:{value1}\ntuple value 2:{value2}\ntuple value 3:{value3}")


