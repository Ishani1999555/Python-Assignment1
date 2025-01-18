"""
2.	Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""
import random

number = random.randint(1,9)
guess_value = int(input("Enter the number (between 1 and 9):"))

while guess_value:
    if number == guess_value:
        print("Well guessed!")
        break

    else:
        print("Guess is incorrect! Try Again")
        guess_value = int(input("Enter the number (between 1 and 9):"))



