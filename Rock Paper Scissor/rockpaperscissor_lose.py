goodbye = False
objects = ["Rock", "Paper", "Scissor"]
point = 0

print("Welcome to Rock Paper Scissor")
while not goodbye:
    my_choice = int(input("1. Rock\n2. Paper\n3. Scissor\nPick a number: "))

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
    
    again = ""
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
