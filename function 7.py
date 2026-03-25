def ispalindrome(s):
    s=s.replace(" "," " ).lower()
    return s==s[::-1]
text = input("Enter a string :")

if ispalindrome(text):
    print("It is Palindrome.")
else:
    print("Not a Palindrome")
