# Program to find largest element in a list dt. 14th Feb 2019
n = int(input("how many numbers you want to enter: "))
num = []
for i in range(0, n):
    num.append(int(input("Enter number: ")))
print("List of numbers is: ")
print(num)
for a in range(1, n):
    if num[0] > num[a]:
        continue
    else:
        num[0], num[a] = num[a], num[0]
print(f"{num[0]} is the largest number")
