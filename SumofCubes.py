# To print sum of cubes of first n natural numbers
n = int(input("How many numbers: "))
cu = 0
for i in range(n+1):
    cu += (i**3)
print("Sum of cubes is " + str(cu))
