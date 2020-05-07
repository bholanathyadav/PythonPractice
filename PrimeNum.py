# To print all prime numbers occurring between two different numbers dt. 12th Feb 2019
# Also to check if a number is prime dt 12th Feb 2019
num = int(input("Enter a number: "))
x = 0
for i in range(1, num+1):
    if num%i == 0:
        x += 1
if x == 2:
    print("It's a prime number\n")
else:
    print("It's not a prime number\n")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("All the prime numbers are here: \n")
for i in range(a,b+1):
    count = 0
    for j in range(1,i+1):
        if (i%j) == 0:
            count += 1
    if count == 2:
        print(i, end = ' ')
