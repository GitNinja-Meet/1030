# 3.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Example usage
result = add(5, 3)
print("Addition:", result)

result = subtract(5, 3)
print("Subtraction:", result)

result = multiply(5, 3)
print("Multiplication:", result)

result = divide(5, 3)
print("Division:", result)
