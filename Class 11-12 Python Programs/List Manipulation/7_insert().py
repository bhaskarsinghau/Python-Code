# insert function insert an item at given position.
# List.insert(<index>,<item>)

a = ['a','e',2,3,'q']
b = a.insert(2,'w')
print(a)

# Output: ['a', 'e', 'w', 2, 3, 'q']

# insert function insert an item at the end of the given list.insert()
# List.insert(len(),<item>)

a = ['a','e',2,3,'q']
b = a.insert(len(a),'w')
print(a)
# Output: ['a', 'e', 2, 3, 'q', 'w']