def convert(s):
    words=s.split()
    return " ".join(sorted(set(words)))

text =input("Enter a sentence:")
print("Result: ",convert(text))
