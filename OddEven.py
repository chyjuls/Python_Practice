# Print all odd or even numbers within a range using the for loop:

OddNumber = [x for x in  range(50) if x % 2 ==1]
print(*OddNumber, sep = "\n")

print("\t")

EvenNumber = [x for x in  range(50) if x % 2 == 0]
print(*EvenNumber, sep = "\n")