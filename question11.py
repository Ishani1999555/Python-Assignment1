"""
11.	Write a  Python program to construct the following pattern, using a nested loop number.
"""

def pattern(rows):
    for i in range(1,rows+1):
        for j in range (i):
            print(i, end="")
        print()

row_number = int(input("Enter the number of rows:"))
pattern(row_number)
