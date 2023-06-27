# Find the greater number

a = float(input("Enter the first Number: "))
b = float(input("Enter the Second Number: "))
c = float(input("Enter the Third Number: "))

# Conditions
if (a>b) and (a>c):
    print("The Greater No.is ",a)
if (b>a) and (b>c):
    print("The Greater No.is ",b)
else:
    print("The Greater No.is ",c)        