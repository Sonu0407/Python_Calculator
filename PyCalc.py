print("This is py calculator")

test = input("You want to calculate? type 'yes' or 'no' ")

isGame = True if test == "yes" else False

gameCount = 0

while (isGame):
    # Task 1 Implement adding in the calculator
    print()
    print(f"What Do you want to do {"now" if gameCount > 0 else ""}?\n"
    "Type '1' for Addition\n"
    "Type '2' for Subtraction\n"
    "Type '3' for Multiplication\n"
    "Type '4' for Division\n"
    "Type 'stop' to exit")

    type = input("Please enter your input here ")
    print()

    if type == "1":
        # start adding logic
        a = int(input("Enter your first number to 'Add' "))
        b = int(input("Enter your second number to 'Add' "))
        print(a + b)
        gameCount += 1
    elif type == "2":
        a = int(input("Enter your first number to 'Subtract' "))
        b = int(input("Enter your second number to 'Subtract' "))
        print(a - b)
        gameCount += 1
    elif type == "3":
        a = int(input("Enter your first number to 'Multiply' "))
        b = int(input("Enter your second number to 'Multiply' "))
        print(a * b)
        gameCount += 1
    elif type == "4":
        a = int(input("Enter your first number to 'Divide' "))
        b = int(input("Enter your second number to 'Divide' "))
        print(a / b)
        gameCount += 1
    elif type == "stop":
        # isGame is false
        isGame = False
        



