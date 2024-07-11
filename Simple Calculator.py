# Simple Calculator 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def calculator():
    while True:
        print("\n----------------------------Welcome to the Simple Calculator!--------------------------------")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("----Select operation:-----")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            result = add(num1, num2)
            operation = "addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "division"
        elif choice == '5':
            result = modulus(num1, num2)
            operation = "modulus"
        else:
            print("Invalid input")
            continue

        print(f"The result of the {operation} is: {result}")

        # To Ask if the user wants to perform another calculation
        again = input("\nDo you want to perform another calculation? (Y/N): ")
        if again.lower() != 'y':
            print("-----------------------Thank you for using the calculator. Goodbye!--------------------------")
            break

# Run the calculator
calculator()
