#Creating List
a = [2,4,5]
b = ['abc','def']
c = [1,2.0,3,4.0]
d = []  # Empty list

# Nested List
e = [3,4,[5,6],7,8]

# l = list(<sequence>)
f = list('hello')
print(f)

# Output: ['h', 'e', 'l', 'l', 'o']
# the string become list (TypeCasting)
 
g = ('s','c','h','o','o','l') # type(g): Tuple
h = list(g)
print(h)

# Output: ['s', 'c', 'h', 'o', 'o', 'l'] 
# the tuple become list (TypeCasting)

l1 = list(input("Enter the list: "))
print("The Element of List:", l1)

''' 
Output:Enter the list: ew35hello
The Element of List: ['e', 'w', '3', '5', 'h', 
'e', 'l', 'l', 'o']
'''

# Eval Function of python can be used to evaluate
# and retrun the result  of an expression give as 
# String. It only works # on string

i = eval("3+8")
print(i)  #Output: 11

j = eval("3*10")
print(j)  #Output: 30

# Accessing list (By its Indexing)
Vowels = ['a','e','i','o','u']
print(Vowels[0]) # Output: a

# Replace by New Value in the list
# because the list is mutable.

Vowels[0] = 1
print(Vowels) 

# Output: [1, 'e', 'i', 'o', 'u']
# a is replace by 1.

Vowels[-4] = 'E'
print(Vowels) 

# Output: [1, 'E', 'i', 'o', 'u']
# e is replace by E.

# Comparing the List
k,l = [1,2,3] , [1,2,3]
M = [1,[2,3]]
print(k == l)     # Output: True
print(k == M)     # Output: False

# List Operator 

# Concatenation +
l1 = [1,3,5]
l2 = [6,7,8]
print("The sum of",l1,"and",l2,"is: ",l1+l2)        
# Output: The sum of [1, 3, 5] and [6, 7, 8] is: 
# [1, 3, 5, 6, 7, 8]

l1 += "abc"
print(l1)  # Output: [1, 3, 5, 'a', 'b', 'c'] 

# Replication *
l1 = [1,3,5]
l2 = 3 # Note that always numeric data
print("The Multiplication of",l1,"and",l2,"is: ",l1*l2)
# Output: The Multiplication of [1, 3, 5] and 3 is:
# [1, 3, 5, 1, 3, 5, 1, 3, 5]

# Slicing the List
# seq = l[start:stop-1:step]

list = [10,12,14,20,22,24,30,32,34]

print(list[0:10:2])  # Output: [10, 14, 22, 30, 34]
print(list[::3])     # Output: [10, 20, 30]
print(list[3:-3])    # Output: [20, 22, 24]

# Using Slices for List Modification
l1 = ["ONE","TWO","THREE"]
l1[0:2] = [1,2]
print(l1)            # Output: [1, 2, 'THREE']

l1[0:2] = "a"
print(l1)            # Output: ["a", 'THREE']

n = [1,2,3]
n[2:] = "604"
print(n)             # Output:[1, 2, '6', '0', '4']

# n[2:] = 604 , cause error.
# type error : can only assign an iterable

# Making true copy
a = [1,2,3]
b = a
print(b)             # Output:[1, 2, 3]

# In case you change the value in a then it should 
# applied on b also because of b = a 
a[1] = 5
print(a ,b) #Output:[1, 5, 3] [1, 5, 3]


c = [1,2,3]
d = list(c)
a[1] = 5 
print(d)

#Page No: 382 
# SIR Why it cause error: 'list' object is not callable


# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com