def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        op = input("Enter the operation (+, -, *, /): ")
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("❌ Invalid operation. Please choose from +, -, *, /.")

def calculator():
    print("🔢 Simple Python Calculator")
    print("---------------------------")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    # Perform calculation
    if operation == '+':
        result = num1 + num2
        print(f"✅ Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"✅ Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"✅ Result: {num1} * {num2} = {result}")
    elif operation == '/':
        while num2 == 0:
            print("❌ Cannot divide by zero.")
            num2 = get_number("Please enter a non-zero second number: ")
        result = num1 / num2
        print(f"✅ Result: {num1} / {num2} = {result}")

# Run the calculator
calculator()
