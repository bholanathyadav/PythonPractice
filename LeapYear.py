# Program to find if a year is Leap Year
y = int(input("Please enter the year you want to check: "))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("Its a leap year")
        elif y % 400 != 0:
            print("Its not a leap year")
    else:
        print("Its a leap year")
