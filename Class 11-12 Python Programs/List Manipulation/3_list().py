# list([<Sequence>])

a = ("Hello")
b = list(a)
print("Type Casting Str become list:",b)
# Output: Type Casting Str become list: ['H', 'e', 'l', 'l', 'o']

c = ('s','c','h','o','o','l') # type(g): Tuple
d = list(c)
print("Type Casting tuple become list:",d)
# the tuple become list (TypeCasting)
# ['s', 'c', 'h', 'o', 'o', 'l']

e = list({'a':101,'b':201})
print("Type Casting Dict become list:",e)
# Output: Type Casting Dict become list: ['a', 'b']

f = list(input("Enter the list: "))
print("The Element of List:", f)

# Output: Enter the list: dfkjaf35
# The Element of List: ['d', 'f', 'k', 'j', 'a', 'f', '3', '5']


# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com