string=input("Enter a string")

print("Forward order:")
i=0
while i< len(string):
    print(string[i],end='')
    i+=1
print("\n")

print("Reverse order:")
i=len(string)-1
while i>=0:
    print(string[i],end='')
    i-= 1
