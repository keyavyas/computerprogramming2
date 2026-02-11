import random
x=int(input("Enter the number"))

L=[]

for i in range(20):
    a=random.randint(1,100)
    L.append(a)
print("The list is",L)
count=0
for i in range (20):
    if x==L[i]:

        count=count+1


print("The number if occurances is: ",count)
