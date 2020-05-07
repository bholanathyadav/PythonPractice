# Program to print Fibonacci numbers dt. 13th Feb 2019
import math
n = int(input("How many fibonacci numbers you want to print: "))
a = 1
b = 2
temp = 0
for i in range(n+1):
    temp = a
    a = b
    b = temp+a
    print(b, end=" ")
print('\n')

# without using 3rd variable
x = 1
y = 2
for i in range(n+1):
    y = x+y
    print(y, end=' ')
    x = y - x
