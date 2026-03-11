para=input("Enter a paragraph:")

words=set(para.split())

print("Unique words: ",words)
print("Number of unique words:",len(words))

s1=input("Enter first sentance: ")
s2=input("Enter second sentance: ")

set1=set(s1.split())
set2=set(s2.split())

common=set1.intersection(set2)

print("common words:",common)
