# Palindrome exercise
# define a palindrome: any word/phrase which returns the same spelling, when spelt backwards:
# hannah
# madam
# noon
# racecar

# Many methods to writing this code but I choose a simpler method:
# using the reverse function/slicing  and the if statement.
# lower() converts all words to small letters.
# Having a capital letter in the palindrome, may return a false output.

word1 = input("Give me a word:..")
word1 = word1.lower()


def reverse(word):
    return word[:: -1]


if reverse(word1) == word1:
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")

# you can also write the if statement like this: if (word1[::-1]==word1):

# end of code!
