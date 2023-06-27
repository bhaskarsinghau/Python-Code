def isStringPalindrome(str):
  if len(str)<=1:
    return True
  else:
    if str[0]==str[-1]:
       return isStringPalindrome(str[1:-1])
    else:
       return False
#__main__
s=input("Enter the string : ")
y=isStringPalindrome(s)
if y==True:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")
