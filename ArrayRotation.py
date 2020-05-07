# Program to rotate an array by n number of elements
h = int(input("How many numbers you want to enter: "))
n = int(input("By how many elements you want to rotate the list: "))
num = []
for i in range(0, h):
    num.append(int(input("Enter number: ")))
print("Here is the list: ")
print(num)
temp = []
for i in range(0, n):
    temp.append(num[0])
    for j in range(0, h-1):
        num[j] = num[j+1]
    num[h-1] = temp[0]
    del(temp[0])
print(num)
