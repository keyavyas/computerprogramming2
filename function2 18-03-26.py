def compute(n):
           n_str=str(n)

           n=int(n_str)
           nn=int(n_str*2)
           nnn=int(n_str*3)
           nnnn=int(n_str*4)

           total= n+nn+nnn+nnnn
           return total 

n=int(input("Enter  a digit:"))



for i in range (4,8):
           result=compute(i)
           print(result)
