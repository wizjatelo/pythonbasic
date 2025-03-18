print ('WELCOME TO A BASIS CALCULATER !!!! ')
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation not in ['+', '-', '*', '/']:
    print("Invalid operation. Please enter +, -, *, or /.") 
    exit()

try:
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    exit()

def format_number(n):
    return int(n) if n.is_integer() else n

formatted_num1 = format_number(num1)
formatted_num2 = format_number(num2)
formatted_result = format_number(result)

print(f"{formatted_num1} {operation} {formatted_num2} = {formatted_result}")
