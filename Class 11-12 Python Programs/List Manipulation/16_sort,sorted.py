# What is main difference b/w sort and sorted ?
a = ['e','i','a','u','o']
b = a.sort()
print("Ascending",a)
# Output: Ascending ['a', 'e', 'i', 'o', 'u']

c = a.sort(reverse = True)
print("Decending",a)
# Output: Decending ['u', 'o', 'i', 'e', 'a']

# Sort: It does not create new list.
# It modifies the existing list.
# It does not returns anything; It just modifies the list.
# and sort is not defined for complex number.

a = ['e','i','a','u','o']
b = sorted(a)
print("Ascending",b)
# Output: Ascending ['a', 'e', 'i', 'o', 'u']

c = sorted(a,reverse = True)
print("Decending",c)
# Output: Decending ['u', 'o', 'i', 'e', 'a']

# Sorted: It create new list.
# It does not modifies the existing list. The list passed as a parameter
# It returns a newly created storted list ; It does not changed the passed sequence.
# and sort is not defined for complex number.


# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com