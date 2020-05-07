# A program to find area of geometric shapes dt. 12th Feb 2019
choice = {1: 'Circle', 2: 'Rectangle', 3: 'Square', 4: 'Triangle'}
print(choice)
ch = int(input("Enter the geometric shape of your choice: "))
if ch==1:
    print("You have chosen to calculate area of a circle!!")
    r = int(input("Enter radius of a circle: "))
    area = 22/7*(r**2)
    print("Area of circle is " + str(area))
elif ch==2:
    print("You have chosen to calculate area of a rectangle!!")
    ln = int(input("Enter length of rectangle: "))
    br = int(input("Enter breadth of rectangle: "))
    area = ln*br
    print("Area of rectangle is " + str(area))
elif ch==3:
    print("You have chosen to calculate area of a square!!")
    sd = int(input("Enter side of a square: "))
    area = sd**2
    print("Area of square is " + str(area))
elif ch==4:
    print("You have chosen to calculate area of a triangle!!")
    base = int(input("Enter base of a triangle: "))
    ht = int(input("Enter height of a triangle: "))
    area = 1/2*base*ht
    print("Area of a triangle is " + str(area))
else:
    print("Invalid choice!!!")
