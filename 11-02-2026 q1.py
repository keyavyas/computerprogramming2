import random

L=[]
for i in range(5):
    a=random.randrange(1,100,2)
    L.append(a)
print(L)
L1=[]
for i in range(5):
    b=random.randrange(2,100,2)
    L1.append(b)
print(L1)


L.pop(2)
L.insert(2,L1)
print("after inserting even list at third position")

flat_list=[]
for item in L:
    if isinstance(item,list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

print("Flattened List:")
print(flat_list)
