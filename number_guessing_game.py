import random

while True:
	secret= random.randint(1,10)
	
	print("Welcome to the number guessing between 1 to 10 game....")
	
	tries= 0
	
	while True:
		guess= int(input("Enter your number: "))
		tries= tries+1
		
		if guess == secret:
			print("Congratulations, your guess is right....")
			print("You guess right in",tries,"Attempts...")
			break
		elif guess < secret:
			print("Too low! , Try again.....")
		else:
			print("Too high! , Try again.....")
			
	while True:
		again= input("Wanna guess again? : ")
		
		if again == "yes":
			break
		elif again == "no":
			exit()
		else:
			print("Invalid answer, please only type yes or no....")