# Intro
name = input("Enter your name: ")
print("Hello", name, "Welcome to the number analyzer.")

check = 0

while True:
	
	#error handeling
	while True:
		try:
			number = int(input("Enter your number: "))
			break
		except:
			print("Enter a valid number")
			
	check = check + 1

	if number < 0:
		print("It's a negative number...")
	elif number > 0:
		print("It's a positive number...")
	else:
		print("It's zero...")
		
	if number < 10:
		print("Small number")
	elif number > 100:
		print("Big number")
	else:
		print("Medium number")

	if number % 2 == 0:
		print("It's an even number")
	else:
		print("It's an odd number")
		
	while True:
		again = input("Wanna check again? yes/no: ").lower()

		if again == "yes":
			break
		elif again == "no":
			print("You checked", check, "times today")
			print("Thank you for using the program...")
			exit()
		else:
			print("Invalid choice, please only type 'yes' or 'no'")
			