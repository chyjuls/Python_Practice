# Sum of numbers of range iteration using while nested loop:
i = 9
while i >= 0:
    j = 0
    add = 0
    # Make sure you replace 10, with i as you are iterating through i...

    while j <= i:
        add += j
        j += 1
    print("sum:", add)
    i -= 1

# variable add  will be  the sum of range of 0-9, 0-8, 0-7, etc.
