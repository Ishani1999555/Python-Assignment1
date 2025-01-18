"""
17.	Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
"""

def remove_elements(result):
    del result[5]
    del result[4]
    del result[0]
    print("The updated list after deletion is: ", result)


input_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
remove_elements(input_list)
