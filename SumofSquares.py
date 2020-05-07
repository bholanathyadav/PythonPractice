# To print sum of squares of first n natural numbers dt 13th Feb 2019
n = int(input("How many numbers: "))
sq = 0
for i in range(n+1):
    sq += (i**2)
print("Sum of squares is: " + str(sq))
