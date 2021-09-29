import random
goodbye = False
objects = ["Rock", "Paper", "Scissor"]
point = 0

print("Welcome to Rock Paper Scissor")
while not goodbye:
	my_choice = int(input("1. Rock\n2. Paper\n3. Scissor\nPick a number: "))
	bot_choice = random.randint(0,2)
	
	print("\nYour choice is", objects[my_choice-1])
	print("Computer choice is", objects[bot_choice])
	print("")
	
	print(objects[my_choice-1], "vs", objects[bot_choice])
	if my_choice == 1 and bot_choice == 1:
		print("Winner is Computer!")
		point -= 1
	elif my_choice == 1 and bot_choice == 2:
		print("Winner is You!")
		point += 1
	elif my_choice == 2 and bot_choice == 0:
		print("Winner is You!")
		point += 1
	elif my_choice == 2 and bot_choice == 2:
		print("Winner is Computer!")
		point -= 1
	elif my_choice == 3 and bot_choice == 0:
		print("Winner is Computer!")
		point -= 1
	elif my_choice == 3 and bot_choice == 1:
		print("Winner is You!")
		point += 1
	else: 
		print("Awww, it's a draw...")
	print("\nYour current point is", point)
	
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
