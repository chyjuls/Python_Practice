# sum of range of numbers using user input.input()

UserNum = int(input("Enter a number..."))
SumNum = 0
for num in range(1, UserNum + 1, 1):
 SumNum = SumNum + num
print("The sum of first ", UserNum, "is", SumNum)

# To find the average of a range of numbers 

Average = SumNum/UserNum
print(Average)