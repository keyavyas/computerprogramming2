def count_lower_upper(s):
    result={"uppercase": 0, "lowercase": 0}

    for ch in s:
        if ch.islower():
           result['uppercase']+=1
        elif ch.isupper():
            result['lowercase']+=1

    return result

str1=input("enter string")
result=count_lower_upper(str1)

print("original string",str1)
print(result)

