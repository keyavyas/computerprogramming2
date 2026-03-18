def create_array(x,y,z,value):
    arr=[[[value for k in range(z)] for j in range(y)] for i in range(x)]
    return arr

x=int(input("Enter first dimension:"))
y=int(input("Enter second dimension:"))
z=int(input("Enter third dimension:"))
val=int(input("enter value to initialize array:"))

array_3d = create_array(x,y,z,val)

for i in range(x):
    print(f"\nlayer {i+1}: ")
    for j in range(y):
           print(array_3d[i][j])
