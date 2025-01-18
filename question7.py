"""
7.	Write a Python program that iterates the integers from 1 to 50.
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
For numbers that are multiples of three and five, print "FizzBuzz".
"""

for numbers in range(0,51):
    if(numbers%3==0):
        if(numbers%5==0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif(numbers%5==0):
        print("Buzz")
    else:
        print(numbers)
print()

