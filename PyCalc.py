import calculatorPattern
from num2words import num2words

print("This is py calculator")

print()
calculatorPattern.dinoPattern()
print()

test = input("You want to calculate? type 'yes' or 'no' ")

isGame = True if test == "yes" else False

gameCount = 0

while (isGame):
    # Task 1 Implement adding in the calculator
    print()
    print(f"What do you want to do {"now" if gameCount > 0 else ""}?\n"
    "Type '1' for Addition\n"
    "Type '2' for Subtraction\n"
    "Type '3' for Multiplication\n"
    "Type '4' for Division\n"
    "Type '5' for Modulo\n"
    "Type '6' for Salary_Calculator\n"
    "Type '7' for Average_Calculator\n"
    "Type 'stop' to exit")

    print()
    type = input("Please enter your input here ")
    print()

    if type == "1":
        # start adding logic
        a = int(input("Enter your first number to 'Add' "))
        b = int(input("Enter your second number to 'Add' "))
        print()
        print(f"Answer = {a + b}")
        print()
        print("*" *100)
        gameCount += 1
    elif type == "2":
        a = int(input("Enter your first number to 'Subtract' "))
        b = int(input("Enter your second number to 'Subtract' "))
        print()
        print(f"Answer = {a - b}")
        print()
        print("*" *100)
        gameCount += 1
    elif type == "3":
        a = int(input("Enter your first number to 'Multiply' "))
        b = int(input("Enter your second number to 'Multiply' "))
        print()
        print(f"Answer = {a * b}")
        print()
        print("*" *100)
        gameCount += 1
    elif type == "4":
        a = int(input("Enter your first number to 'Divide' "))
        b = int(input("Enter your second number to 'Divide' "))
        print()
        print(f"Answer = {a / b}")
        print()
        print("*" *100)
        gameCount += 1
    elif type == "5":
        a = int(input("Enter your first number to 'Modulo' "))
        b = int(input("Enter your second number to 'Modulo' "))
        print()
        print(f"Answer = {a % b}")
        print()
        print("*" *100)
        gameCount += 1
    elif type == "6":
        salary = int(input("Enter your ctc "))
        monthly = round(salary / 12)
        words = num2words(monthly)
        print()
        print(f"Your monthly salary = {round(salary / 12)} ({words} Only)")
        print()
        print("*" *100)
        gameCount += 1
    elif type == "7":
        nums = list(map(int, input("Enter at least two numbers ").split())) #TODO cover the edge cases tomorrow and make it stable to handle anything wrong input.
        average = sum(nums) / len(nums)
        print()
        print("Average:", average)
        print()
        print("*" *100)
        gameCount += 1
    elif type == "stop":
        # isGame is false
        isGame = False
        



