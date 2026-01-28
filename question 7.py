str=input("Enter a  string")
vowel_count=0
consonant_count=0
length=len(str)

vowels="aeiouAEIOU"

for i in str:
    if i in vowels:
         vowel_count=vowel_count+1
    else:
        consonant_count=consonant_count+1
print("length of string")
print(len(str))
print("no.of vowels")
print(vowel_count)
print("no of consonants")
print(consonant_count)
