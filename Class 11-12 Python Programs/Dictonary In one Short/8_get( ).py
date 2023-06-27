# This function simply return the value of the required Key. for example:

A = {1 : "One", 2 : "Two", 3 : "Three"}
B = {'A' : "Apple", 'B' : "Bat", 'C' : "Cat", 'D' : "Doll"}
print(A.get(2))
print(B.get('C'))
print(A.get(4)) #This key is not available in dictionary A so return NONE
print(A.get(4),"Key Not Found") #We can specify our message to display if key not found

''' Output:
Two
Cat
None
None Key Not Found
'''
# NOTE: If key is not available in dictionary then this method will return None or customized 
# message as shown above:  None Key Not Found

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com