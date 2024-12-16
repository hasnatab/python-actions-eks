import argparse

# Define a function for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Parse the command-line arguments
parser = argparse.ArgumentParser(description="Simple calculator")
parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help="Operation to perform")
parser.add_argument('a', type=float, help="First operand")
parser.add_argument('b', type=float, help="Second operand")

# If no arguments are passed, set default values
args = parser.parse_args()

if not args.operation:
    args.operation = 'add'
    args.a = 2
    args.b = 3

# Perform the operation based on the parsed arguments
if args.operation == 'add':
    result = add(args.a, args.b)
elif args.operation == 'subtract':
    result = subtract(args.a, args.b)
elif args.operation == 'multiply':
    result = multiply(args.a, args.b)
elif args.operation == 'divide':
    result = divide(args.a, args.b)

# Print the result
print(f"Result: {result}")
