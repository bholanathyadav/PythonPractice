# A program to calculate remainder when all the elements of a list multiplied and divided by a number
n = int(input("How many numbers you want to enter in list: "))
d = int(input("Enter the divisor: "))
rem = 1
# tot = 1
num = []
for i in range(0, n):
    num.append(int(input("Enter number: ")))
for i in range(0, n):
    rem *= num[i] % d
if rem > 0:
    print("The remainder will be " + str(rem % d))
else:
    print("Multiple of all numbers is completely divisible")
