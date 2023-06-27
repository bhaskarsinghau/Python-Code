'''
This function merge the key value air of two dictionary into one. In simple words it simply 
join/merge the two dictionary. It merge the keys and values of one dictionary into other and
overwrites the values of the same key. for example: '''

#We can not change the key of an element, but can change the value of a respective key as follows:

A = {1 : "One", 2 : "Two", 3 : "Three"}
B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
A.update(B)
print(A)

# Output: {1: 'Amit', 2: 'Sunil', 3: 'Three', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
#It over writes the values of same keys and add the values of different keys

B = {1: 'Amit', 2: 'Sunil', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
B[2] = 'Ram'
print(B)
# OUTPUT: {1: 'Amit', 2: 'Ram', 5: 'Lata', 6: 'Suman', 7: 'Ravi'}
# #It over writes the values of same keys and add the values of different keys 

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com
