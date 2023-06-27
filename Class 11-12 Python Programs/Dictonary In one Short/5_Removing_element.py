#There are two ways by which we can delete the elements of dictionary:

# 1.By using del statement : Syntax of using del statement is : del <dictionary-name>[key of element]
B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
del B[2] # It will remove the element of key 2
print(B)

# OUTPUT: {1: 'Amit', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}

'''
B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
del B[3]  # It will return an error (KeyError) if the key given is not present in the dictionary
print(B)

# It will return an error (KeyError) if the key given is not present in the dictionary
KeyError: 3
'''
# 2. By Using pop() function : This function not only delete the element of required key but also return
# the deleted value.

B = {1: 'Amit', 2: 'Anil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
a=B.pop(2) #It returns the element of Key - 2
print(a)
print(B)

# Output:
# Anil
# {1: 'Amit', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}

B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
a=B.pop(6) #It returns the element of Key - 6
print(a)
print(B)

# Output:
# Suman
# {1: 'Amit', 2: 'Sunil', 5: 'Lata', 7: 'Ravi'}

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com