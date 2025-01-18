"""
8.Write a Python program that takes two digits m(row) and n(column) as input and generates a 2D array.
The element value in the i-th row and j-th column of the array should be i*j.
"""

m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Generate and print the 2D array directly
print("Generated 2D Array:")
for i in range(m):
    print([i * j for j in range(n)])
