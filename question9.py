"""
9.Write a Python program to find numbers between 100 and 400 (both included)
where each digit of a number is an even number.
Example: 122 is not the number but 222 is the number because all the digits are even
"""
def find_even_digit_numbers():
    result = []
    for number in range(100, 401):
        is_even = True                      # Assume the number is valid
        for digit in str(number):
            if int(digit) % 2 != 0:         # If a digit is odd
                is_even = False
                break
        if is_even:
            result.append(number)
    return result

even_numbers = find_even_digit_numbers()

print("Numbers where all digits are even between 100 and 400:")
print(even_numbers)



