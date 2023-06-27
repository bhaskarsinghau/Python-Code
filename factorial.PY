def factorial(n):
   if n == 1:
     return n
   else:
     return n*factorial(n-1)
num=int(input("Enter the number: "))
if num < 0:
  print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
  print("The factorial of 0 is 1")
else:
  print("The factorial of ",num," is ", factorial(num))

x = int(input("Enter the number: "))
n = int(input("Enter the number: "))

sum = x
for  i in range(1,n+1):
  if i%2==0:
    print(-(sum**i))
  else:
    print(sum**i)  