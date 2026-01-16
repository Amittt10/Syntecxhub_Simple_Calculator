import math, sys

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

print("Welcome to the Command-Line Calculator!")

num1 = get_number("Enter the first number: ")
while True:
    operation = input("Choose an operation (+, -, *, /) or 'c' for clear or 'q' to quit: ").lower()
    if operation == 'q':
        print("Exiting the calculator. Goodbye!")
        sys.exit()
    elif operation == 'c':
        num1 = get_number("Enter the first number: ")
        continue

    num2 = get_number("Enter the second number: ")
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(e)
            continue
    else:
        print("Invalid operation.")
        continue
    
    print(f"Result: {num1} {operation} {num2} = {result}")

    num1 = result