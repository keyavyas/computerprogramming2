def oddeven (numbers):
    odd_1=[]
    even_1=[]
    for  i in numbers:
        if i%2==0:
            even_1.append(i)
        else:
            odd_1.append(i)


    return odd_1,even_1
           
numbers=[1,2,3,4,5,6,7]
odds,even=oddeven(numbers)
print("list of odd numbers",odds)
print("list of even numbers",even)
