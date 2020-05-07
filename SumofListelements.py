# To input numeric elements in list and determine their sum
n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    num = int(input("Enter number: "))
    a.append(num)

print("List has been populated. Now sum of all numbers entered is: ")
sum = 0
for i in range(n):
    sum += a[i]

print(sum)