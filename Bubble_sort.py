#Bubble sort algorithm using python:

def My_BubbleSort(NumArr):

    for j in range(len(NumArr)-1, 0, -1):
        for i in range(j):
            if NumArr[i] > NumArr[i+1]:
                temp = NumArr[i]
                NumArr[i] =NumArr[i+1]
                NumArr[i+1] = temp
NumArr = [13,22,34,65,78,32,10,15,12,1,2]

My_BubbleSort(NumArr)

print(*NumArr, sep ="\n")
