"""
5.	Write a Python program to count the number of even and odd numbers in a series of numbers
"""
def even_odd_count(series):
    even_cnt = 0
    odd_cnt = 0
    for i in series:
        if i%2 ==0:
            even_cnt +=1
        else:
            odd_cnt +=1
    print("Number of even numbers = ", even_cnt)
    print("Number of odd numbers = ", odd_cnt)

number_series = [1,2,3,4,5,6,7,8,9]
even_odd_count(number_series)


