print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")

# second typ
first=int(input("Enter first value: "))
operater=input("Enter operater (+,-,*,/,%): ")
second=int(input("Enter second value: "))

if operater == "+":
    print(first+second)
elif operater == "-":
    print(first-second)
elif operater == "*":
    print(first*second)
elif operater == "/":
    print(first/second)
elif operater == "%":
    print(first%second)
else:
    print("invalid process")