# Palindrome exercise
# define a palindrome: any word/phrase which returns the same spelling, when spelt backwards:
# hannah
# madam
# noon
# racecar

# Using python, we can tell which words/phrases are palindromes.
# one way to do this is by using the reverse function (you can also the slice function)

# define your function


def my_palindrome(w):
    w = w.lower()

    return w == w[::-1]


# lets try some words and see if any is palindrome

wrd_1 = "hannah"
wrd_2 = "racecar"
wrd_3 = "nothing"
print(my_palindrome(wrd_1))
print(my_palindrome(wrd_2))
print(my_palindrome(wrd_3))


