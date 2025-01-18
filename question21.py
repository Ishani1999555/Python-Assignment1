"""
21.	Write a Python program to get the frequency of elements in a list.
"""

def find_frequencies(count_list):
    """Find the frequency of each element in a list."""
    frequency_list = []
    element_list = []

    for element in count_list:
        if element not in element_list:
            count = count_list.count(element)
            frequency_list.append((element,count))
            element_list.append(element)
    return frequency_list

elements = list(input("Enter the elements of the list (comma separated): ").split(","))

frequencies = find_frequencies(elements)

for value, frequency in frequencies:
    print(f"List element {value} frequency: {frequency}")
