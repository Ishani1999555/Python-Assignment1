"""
15.	Write a program to check whether a given string is a palindrome or not.
Palindrome words have the same spelling if you reverse the string.
Eg: Dad is a palindrome because it is the same when you reverse it.
"""
def is_palindrome(string):
    string = string.lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        print("It is a palindrome string")
    else:
        print("Not a palindrome string.")

#input string
input_string = input("Enter a string: ")
is_palindrome(input_string)
