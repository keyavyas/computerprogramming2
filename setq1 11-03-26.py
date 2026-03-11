s1={'Math','Physics','Chemistry'}
s2={'Physics','Biology','Math'}

common=s1.intersection(s2)
print("Common subjects: ",common)

only_first=s1-s2
print("First student: ",only_first)

only_second=s2-s1
print("Second student: ",only_second)

total_unique=s1.union(s2)
print("Total unique subjects: ",total_unique)
