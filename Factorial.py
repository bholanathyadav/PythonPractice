# A program to calculate factorial of a number dt. 12th Feb 2019
n = int(input("Enter a number of your choice: "))
fact = 1
for i in range(1, n+1):
    fact *= i

print("Factorial of {0} is {1}".format(n,fact))
