# Independent Copy

a = [1,2,3]
b = list(a)
a[1] = 5 
print(b)
# Output: [1, 2, 3]

a = [1,2,3]
b = a.copy()
a[1] = 5 
print(b)
# Output: [1, 2, 3]
