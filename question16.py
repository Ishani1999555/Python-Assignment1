"""
16.	Write a program to check whether a given number is a palindrome. Eg: 101 is a palindrome
"""

def palindrome_number(number):
    org_number = str(number)
    reversed_number = org_number[::-1]
    if reversed_number == org_number:
        print(f"the input number {number} is a palindrome!")
    else:
        print(f"the input number {number} is not a palindrome!")

value = int(input("Input a number:"))
palindrome_number(value)
