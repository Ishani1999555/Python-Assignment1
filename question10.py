"""
10.	Write a Python program to create the multiplication table (from 1 to 10) of a number.
"""

def multiplicationtable(number):
    multiplier = 1
    answer = 0
    while multiplier<=10:

        answer = number*multiplier
        print(f'{number}*{multiplier}={answer}')
        multiplier+=1

value = int(input("Input a number:"))
multiplicationtable(value)
