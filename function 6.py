def create_list(n):
    return[(x,x**2,x**3)for x in range(1,n+1)]

n=int(input("enter the ending value:"))
print(create_list(n))
