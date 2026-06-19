history = []
try:
	with open("calculator.txt","r") as file:
		for line in file:
			history.append(line.strip())
except:
	pass
print("—"*30)
print(" "*9,"CALCULATOR"," "*9)
print("—"*30)

print("Previous History:")
for i in history:
    print(i)
print("—"*30)

def calculator(a,b,op):
	if op == "+":
		return a+b
	elif op == "-":
		return a-b
	elif op == "*":
		return a*b
	elif op == "/":
		if b == 0:
			return "Cannot divide by 0"
		else:
			return a/b
	else:
		return "Invalid operator"
		
while True:
    print("Calculator running...")
    
    while True:
        try:
            a = int(input("Enter your first number: "))
            break
        except:
            print("Invalid input, try again...")

    while True:
        try:
            b = int(input("Enter your second number: "))
            break
        except:
            print("Invalid input, try again...")

    op = input("Enter operator (+, -, *, /): ")

    result = calculator(a, b, op)
    history.append(f"{a} {op} {b} = {result}")
    print("Result:", result)
    print("\nHISTORY:")
    for i in history:
        print(i)
    print("—" * 30)

    while True:
        again = input("Wanna guess again? 'yes' or 'no': ").lower()
        if again == "yes":
            break
        elif again == "no":
            print("Thnkyou for using my calculator program , see you next time...")
            break
        else:
            print("Please only type 'yes' or 'no'")

    if again == "no":
        with open("calculator.txt", "w") as file:
            for i in history:
                file.write(i + "\n")
        break

print("—"*50)
print(" "*10,"THANKYOU FOR USING MY PROGRAM"," "*10)
print("—"*50)