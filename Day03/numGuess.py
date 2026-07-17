# guessing a number between 1- 100
import random
num = random.randint(1,100)

print("You have only 10 chances to guess the number (1-100)")
for i in range(1,11):
    guess = int(input("Enter the guess number -> "))
    if(guess == num):
        print("Congratulations... ! you got it")
        break
    else:
        if(guess>num):
            print("Your number is higher then the actual number")
        else:
            print("Your number is lower then the actual number")
        print(f"{10-i} chances are left")
    print("")
else:
    print(f"Hard luck! the actual number was {num}")