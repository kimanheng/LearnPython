goodbye = False
objects = ["Rock", "Paper", "Scissor"]
point = 0
again = ""

print("Welcome to Rock Paper Scissor")
while not goodbye:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    my_choice = int(input("Pick a number: "))

    print("")
    print("Your choice is", objects[my_choice-1])
    if my_choice == 1:
        print("Computer choice is Paper")
    elif my_choice == 2:
        print("Computer choice is Scissor")
    elif my_choice == 3:
        print("Computer choice is Rock")

    print("")
    print("You lose!")
    point -= 1
    print("Your current point is", point)

    while again != "n" and again != "y":
        again = input("Play again? Y/N: ")
        again = again.lower()
        if again == "n":
            goodbye = True
        elif again == "y":
            again = ""
            break
        else:
            continue
print("Program has ended")
