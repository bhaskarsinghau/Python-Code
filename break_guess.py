import random
number = random.randint(10,50)
ctr=0
while ctr<5:
    guess = int(input("Guess the Number in range 10....50: "))
    if guess <=9:
        print("Restart the Program. \nPlz input greater than 9 Numbers because range is (10...50)")
        break
    if guess >=51:
        print("Restart the Program. \nPlz input greater Less than 51 Numbers because range is (10...50)")
        break
    if guess == number:
        print("You win!! :)")
        break
    else:
        ctr +=1
if not ctr < 5: #The loop is terminated after 5 iterations
    print("Times Up, You Lose:(\nThe Number was ",number)        