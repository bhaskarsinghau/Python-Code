fin=open("E:\\Some Tricks.txt",'r')
str=fin.read( )
L=str.split( )
count=0
for i in L:
    if i=='a':
       count=count+1
print(count)
fin.close( )
