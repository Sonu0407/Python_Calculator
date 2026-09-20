print("This is py calculator")

test = input("You want to calculate? type 'yes' or 'no' ")

isGame = True if test == "yes" else False

while (isGame):
    # Task 1 Implement adding in the calculator
    print()
    print("What Do you want to do?\n"
    "Type '1' for Addition\n"
    "Type '2' for Subtraction\n"
    "Type 'stop' to exit")

    type = input("Please enter your input here ")
    print()

    if type == "1":
        # start adding logic
        a = int(input("Enter your first number to 'Add' "))
        b = int(input("Enter your second number to 'Add' "))
        print(a + b)
    elif type == "2":
        a = int(input("Enter your first number to 'Subtract' "))
        b = int(input("Enter your second number to 'Subtract' "))
        print(a - b)
    elif type == "stop":
        # isGame is false
        isGame = False
        



