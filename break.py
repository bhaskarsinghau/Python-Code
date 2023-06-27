#Break Statement

a=b=c=0
for i in range(1,21):
    a = int(input("Enter the Number: "))
    b = int(input("Enter the Number: "))
    if b == 0:
        print("Zero Division Error ! Aborting!")
        break
    else:
        c = a//b
        print("Quotient: ",c)
print("Progaram Over") 