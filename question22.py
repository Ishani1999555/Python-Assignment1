"""
22.	Write a program to check whether a letter is a vowel or a consonant
"""

def check_vowel_or_consonant(letter):
    if letter=='a' or letter =='A' or letter=='e' or letter =='E' or letter=='i' or letter =='I' or letter=='o' or letter =='O' or letter=='u' or letter =='U':
        print("the input letter is a vowel!")

    else:
        print("the input letter is a consonant!")

value = str(input("enter a letter:"))
check_vowel_or_consonant(value)


