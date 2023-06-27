# the sort() function sorts the items of the list by 
# default in increasing order.


a = ['e','i','a','u','o']
b = a.sort()
print("Ascending",a)
# Output: Ascending ['a', 'e', 'i', 'o', 'u']

c = a.sort(reverse = True)
print("Decending",a)
# Output: Decending ['u', 'o', 'i', 'e', 'a']
'''
TypeError: '<' not supported between instances of 'int' and 'str'
a = ['e','i',2,'a','u','o']
b = a.sort()
print(a)
'''


# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com