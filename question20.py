"""
20.	Write a Python program to find the second-smallest number in a list.
"""

def second_smallest(number_lst):
    number_lst.sort()
    if len(number_lst) < 2:
        print("The List must contain at least two distinct elements.")
        return 0

    # Find the first unique 2nd smallest number
    min_number = number_lst[0]
    for num in number_lst:
        if num > min_number:
            print("The second smallest number is:", num)
            return 0
    print("No second smallest number: All elements are the same.")

# Input list
number = list(input("enter the values(comma separated):").split(","))
second_smallest(number)

