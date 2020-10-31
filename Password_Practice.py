# Steps
# Ask user to enter password
# define password complexity using, minimum length, use of alphanumeric characters,and capital letters.
# minimum length = 12
# At least one number
# At least one capital letter
# use the regex function

# Ask user to re-enter password
# using if statements and boolean operators
# define password length, use of upper cases and numbers.
# import the regix function.


import re


def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 12:
            print("Make sure your password is at lest 12 letters")
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password seems fine")
            break


validate()
