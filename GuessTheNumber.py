import random
number = random.randint(1, 15)
guess = ()
while guess != number:
    guess = int(input("Guess The Number (1-15): "))
    if guess == number:
        print("Congratulation! You Guess The Right Number!")
    else:
        if guess > number:
            print("Your Guess is Too High, Try Again")
        else:
            print("Your Guess is Too Low, Try Again")
