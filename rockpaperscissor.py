import random
goodbye = False
object = ["Rock", "Paper", "Scissor"]
point = 0
again = ""

print("Welcome to Rock Paper Scissor")
while not goodbye:
	print("1. Rock")
	print("2. Paper")
	print("3. Scissor")
	my_choice = int(input("Pick a number: "))
	bot_choice = random.randint(0,2)
	print("")
	
	print("Your choice is", object[my_choice-1])
	print("Computer choice is", object[bot_choice])
	print("")
	
	print(object[my_choice-1], "vs", object[bot_choice])
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
	print("")
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
