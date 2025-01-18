"""
6.	Write a  Python program to get the Fibonacci series between 0 and 50.
"""
a = 0
b = 1

# Print a message
print("Fibonacci Series between 0 and 50:")

# Generate and print Fibonacci numbers
while a <= 50:
    print(a, end=" ")
    temp = a+b  #temporary variable assigned in order to update the value
    a = b
    b = temp
    temp = b


