set1=set(input("Enter elements of first set:").split())
set2=set(input("Enter elements of second set:").split())

print("First set is subset of second:",set1.issubset(set2))

print("Second set is superset of first:",set2.issuperset(set1))

print("Both sets are equal: ",set1==set2)
