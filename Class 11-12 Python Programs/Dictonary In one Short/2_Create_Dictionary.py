'''
Write a program to enter roll number and Names of five students 
and store the data in dictionary.

'''
d = { }
for i in range(5):
     Rollno=int(input("Enter Roll number:"))
     name=input("Enter Name of student:")
     d[Rollno] = name
print(d)

'''Output:
Enter Roll number:1
Enter Name of student:Aman Singh
Enter Roll number:6
Enter Name of student:Bhaskar Singh
Enter Roll number:7
Enter Name of student:Chandan Srivastav
Enter Roll number:19
Enter Name of student:Vishwas Singh
Enter Roll number:20
Enter Name of student:Starlink
{1: 'Aman Singh', 6: 'Bhaskar Singh', 7: 'Chandan Srivastav', 19: 'Vishwas Singh', 20: 'Starlink'}
'''

# Created By: Bhaskar Singh with the help of Visual Studio Code.
# Visit: starlink.atwebpages.com