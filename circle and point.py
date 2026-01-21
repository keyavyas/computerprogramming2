import math
x=int(input("Enter x-coordinate of centre  "))
y=int(input("Enter y-coordinate of centre "))
r=int(input("Enter radius of circle "))
x1=int(input("Enter x-coordinate of point "))
y1=int(input("Enter y-coordinate of point "))

distance = math.sqrt(pow(x1-x,2)+pow(y1-y,2))

if distance<r:
    print("Point lies inside the circle")
elif distance==r:
    print("Point lies on the circle")
else:
    print("Point lies outside the circle")
