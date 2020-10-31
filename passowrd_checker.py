# STEPS:
# Define your function:password_strength
# Ask user to enter password
# define password complexity using, minimum length, use of alphanumeric characters,and capital letters.
# minimum length = 8
# At least one number
# At least one capital letter
# use the regex function
# Using the while loop:
# ask user to re-enter password
# until a strong password is achieved.
# import the regEx function.


import re


def password_strength():
    while True:

        password = input("Please enter your password:")

        if not (not (len(password) < 8) and re.search(r"[A-Z]", password)):

            print("This is a weak password, make sure your password is at least 8 letters,with at least a capital "
                  "letter.")

        elif not re.search(r"[\d]+", password):
            print("Medium, please add a number...")

        else:
            print("This password is strong")
            break


password_strength()

# For use of the regular expression syntax(reGex)vist https://docs.python.org/3/library/re.html
