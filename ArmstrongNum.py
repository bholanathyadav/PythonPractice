# A program to find if a number is an Armstrong number dt. 12th Feb 2019
num = int(input("Enter a number of your choice: "))
a = str(num)
b = len(a)
arm = 0
for i in a:
    c = int(i)
    arm += c**b

if num == arm:
    print("Yes, it is an Armstrong number")
else:
    print("No, it is not an Armstrong number")
