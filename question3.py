"""
3.	Write a  Python program to construct the following pattern, using a nested for loop.
Bonus : Make it dynamic by asking the user number of rows.

"""

def pattern(rows):
    for i in range(1,rows+1):
        for j in range (i):
            print("*", end="")
        print()

row_number = int(input("Enter the number of rows:"))
pattern(row_number)
