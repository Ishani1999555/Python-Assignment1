"""
19.	Write a Python program to append a list to the second list.
"""

def list_append(l1,l2):
    l1.extend(l2)
    print("the appended list is :", l1)

list1 = list(input("enter the elements for List 1:").split(","))
list2 = list(input("enter the elements for List 2:").split(","))
list_append(list1,list2)
