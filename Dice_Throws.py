import random as r
n = int (input ("How many throw you wants: "))
for i in range (1, n+1):
    print("Throw", i, ":", r.randint(1,6))