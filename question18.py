"""
18.	Write a program to check whether a number is prime or not.
"""
#import sympy
from mpmath.libmp import isprime

number = int(input("Enter a number:"))

if isprime(number) is True:
    print(f"The input value {number} is a Prime Number.")
else:
    print(f"The input value {number} is Not a Prime Number.")

