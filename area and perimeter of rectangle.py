a=int(input("Enter length "))
b=int(input("Enter breath "))

area=a*b
perimeter=2*(a+b)

if area > perimeter:
    print("Area is greater than perimeter")
else:
    print("Area is not greater than perimeter")
