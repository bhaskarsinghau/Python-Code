fin=open("E:\Some Tricks.txt",'r')
L1=fin.readlines( )
s=' '
for i in range(len(L1)):
  L=L1[i].split( )
  for j in L:
   s=s+j
   s=s+'#'
print(s)
fin.close( )
