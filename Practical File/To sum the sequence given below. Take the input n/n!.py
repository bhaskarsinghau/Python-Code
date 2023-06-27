'''
Write a python program to sum the sequence given below. Take the input n
from the user. 1+1/1!+1/2!+1/3!+⋯+1/n!
'''

def fact(x):
  j=1
  res=1
  while j<=x:
    res=res*j
    j=j+1
    return res
n=int(input("Enter the number : "))
i=1
sum=1
while i<=n:
  f=fact(i)
  sum=sum+1/f
  i+=1
print(sum)