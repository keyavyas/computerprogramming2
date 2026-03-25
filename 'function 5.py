def ispangram(s):
    alphaset= set(' abcdefghijklmnopqrstuvwxyz')
    s=s.lower()
    return alphaset <= set(s)

text= input("Enter a sentance:")

if ispangram(text):
    print("The given sentence is a Pangram")
else:
    print("The give sentence is not a Pangram")
