# For each digit in the integer print the corresponding number of *s
num = int(input("Enter a number of your choice: "))
a = str(num)
ch = input("Enter a character of your choice: ")
for i in a:
    print(ch * int(i))
