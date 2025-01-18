"""
14.Write a Python program to get the largest number from a list. Using both loop and max function
"""

def maximum_listvalue(value_list):
    result = max(value_list)
    print("The maximum value in the list:", result)

def maximum_list_withloop(value_list):
    largest = value_list[0]
    for maximum in value_list:
        if largest < maximum:
            largest = maximum           # Update the largest number
    return largest

value = input("Enter the elements of the list(comma separated): ").split(",")
numbers = [int(x) for x in value]

# maximum value in the list with max() function
maximum_listvalue(value)

# maximum value in the list with loop
largest_number = maximum_list_withloop(value)
print("The maximum value in the list(with loop):", largest_number)

