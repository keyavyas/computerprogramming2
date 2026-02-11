import random

numbers=[]
for i in range(20):
    numbers.append(random.randint(1,50))

print("Generated list: ",numbers)

num=int(input("Enter a number: "))

found=False
print("Postions of occurances:")


for i in range(len(numbers)):
    if numbers[i]==num:
        print("Found at:",i)
        found=True

if not found:
    print("Number not found in list.")
