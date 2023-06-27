#.startwith() : retruns true if that string is start with the substring.
#.endswith() : retruns true if that string is end with the substring.

a = 'abcd'

print("startswith cd: ",a.startswith("cd"))
print("startswith ab",a.startswith("ab"))
# Output:startswith cd:  False
# startswith ab True

print()

print("endswith cd: ",a.endswith("cd"))
print("endswith ab: ",a.endswith("ab"))
# Output:endswith cd:  True
# endswith ab:  False