'''
 Write a program to store book id, book name and price 
 of three books and store the data in dictionary named “dict”
'''
dict = {}
for i in range(3):
     b_id = int(input("Enter book id : "))
     b_name = input("Enter book name : ")
     b_price = int(input("Enter price of book : "))
     temp=[b_name,b_price]
     dict[b_id] = temp
print(dict)

''' Output:
Enter book id : 1
Enter book name : Computer Science
Enter price of book : 546
Enter book id : 2
Enter book name : Maths
Enter price of book : 150
Enter book id : 3
Enter book name : Biology
Enter price of book : 150
{1: ['Computer Science', 546], 2: ['Maths', 150], 3: ['Biology', 150]}
'''

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com