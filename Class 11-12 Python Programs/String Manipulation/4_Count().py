a = ("abracadabra")
b = (a.count('ab'))
print(b)
# Output: 2

#a.count('str',start,stop)

a = ("abracadabra")
b = (a.count('ab',4,8))
print(b)
# Output: 0

#a.count('str',start) 

a = ("abracadabra")
b = (a.count('ab',6)) #6th Character Onwards
print(b)
# Output: 1