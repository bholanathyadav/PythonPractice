# program to print largest of three numbers
print('enter three numbers')
a = int(input("Enter first number: "))
b = int(input('Enter second number: '))
c = int(input('enter third number: '))
if a > b:
    if a > c:
        print(str(a) + ' is the greatest number')
    elif c > a:
        print(str(c) + ' is the greatest number')
elif b > c:
    print(str(b) + ' is the greatest number')
else:
    print(str(c) + ' is the greatest number')
# end of program





































