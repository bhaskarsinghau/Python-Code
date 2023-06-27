print() # for spacing

print ( '''Welcome Python User in this arena {Removing Duplicate value and Finding Unique Value From List},
Created by:Bhaskar Singh.''')

print() # for spacing

print('''You all ready heard about it :
To Removing duplicate value we use set function because set is unique.  (Padeh too hoge hi Class 11th Maths ka Ch-1)''')

A = [1, 2, 3, 1 ,3, 2, 4, 5, 6, 4, 7, 5, 8, 5]
B = ("is the list of this coding.")
print("We take Example : ",(A),(B))

#For Removing duplicate value we use set because set is unique.  (Class 11th Maths ka Ch-1)

A = list(set(A))
print("The Unique Value from the above value",(A))

# How to find which number repeted many times

B = max(set(A), key=A.count)
print("The max repeted number is:",(B))

print() # for spacing

print("Now it is time for User Input (User Choice)")

A = list(input("Enter the list: "))
print(A)
A = list(set(A))
print("The Unique Value from the above value",(A))
C = max(set(A), key=A.count)
print("The max repeted number is:",(C))
