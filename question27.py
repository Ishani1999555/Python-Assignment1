"""
27.	Write a  Python program to compute the element-wise sum of given tuples.
"""

def convert_tuple(zero, first, second, third):
    # Create and return a tuple
    result = (zero, first, second, third)
    return result

t_list = []
zero_ele = 0
first_ele = 0
second_ele = 0
third_ele = 0

# Input loop to collect tuples
while True:
    a = input("Enter the tuple (comma-separated values) or 'done' to stop: ")
    if a.lower() == "done":
        break
    t = tuple(map(int, a.split(',')))  # Convert each part of the input to an integer
    t_list.append(t)

# Print the list of tuples
#print("List of tuples:", t_list)

# Calculate the element-wise sum
for i in range(len(t_list)):
    zero_ele += t_list[i][0]
    first_ele += t_list[i][1]
    second_ele += t_list[i][2]
    third_ele += t_list[i][3]

# Print the summed elements as a tuple
result_tuple = convert_tuple(zero_ele, first_ele, second_ele, third_ele)
print("Element-wise sum as a tuple:", result_tuple)



