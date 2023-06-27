#extend method adds multiple item to the end of the list.

a = [1,2,3,'a',2,'e',5]
print("Original list contains",len(a),"elements",a)

# Output: Original list contains 7 elements 
# [1, 2, 3, 'a', 2, 'e', 5]

b = ['d','e',3,4,5]
c = a.extend(b)
print("a.extend(b)",b,"makes",len(a),"elements they are",a)

# Output: a.extend(b) ['d', 'e', 3, 4, 5]
# makes 12 elements they are [1, 2, 3, 'a', 2, 'e', 5, 'd', 'e', 3, 4, 5]