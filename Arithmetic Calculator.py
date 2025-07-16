def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error: Division by zero!"
    return x / y

def calculator():
    print("🧮 Welcome to the Simple Calculator")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Choose operation (+, -, *, /): ")

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("❌ Invalid operator. Please choose from +, -, *, /")
                continue

            print(f"✅ Result: {num1} {op} {num2} = {result}")

        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("👋 Thank you for using the calculator!")
            break

calculator()
