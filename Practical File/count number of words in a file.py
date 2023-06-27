fin=open("E:\\Some Tricks.txt",'r')
str=fin.read( )
L=str.split()
count_words=0
for i in L:
   count_words=count_words+1
print(count_words)
