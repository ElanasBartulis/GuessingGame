import random

random_nub = random.randint(1,10)
user = None

while True:
	user = input("Guess a number ")
	user = int(user)
	if user < random_nub:
		print("Your too low")
	elif user > random_nub:
		print("You are too high")
	else:
		print("User Wins!") 
		play = input("Do you want to play again? (y/n) ")
		if play == "y":
			random_nub = random.randint(1,10)
			play = None
		else:
			print("Thank you for playing")
			break
