# A program to calculate Simple Interest and Compound Interest dt. 12th Feb 2019

p = int(input("Enter principle: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter number of years: "))

si = (p*r*t)/100

print("Simple interest to be paid is: " + str(si))

amount = p*((1+(r/100))**t)
ci = amount - p

print("Compound interest to be paid is: " + str(ci))
