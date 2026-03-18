def  sum_avg(m1,m2,m3,m4,m5):
     total =m1+m2+m3+m4+m5
     average=total/5
     return total,average

marks=[]
for i in range (1,6):
    m=float(input("Enter marks for subject{i}:"))
    marks.append(m)
total,avg=sum_avg(marks[0],marks[1],marks[2],marks[3],marks[4],marks[5])

print(total)
print(avg)

    
