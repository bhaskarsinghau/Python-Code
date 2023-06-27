# This function not only delete the element of required key but also return the deleted value.

B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
a=B.pop(2) #It returns the element of Key - 2
print(a)
print(B)

# Output: Sunil
# {1: 'Amit', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}

B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
a=B.pop(6) #It returns the element of Key - 6
print(a)
print(B)

# Output: Suman
# {1: 'Amit', 2: 'Sunil', 5: 'Lata', 7: 'Ravi'}

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com