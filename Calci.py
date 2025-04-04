# calculator.py

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Unsupported operator"

# Example usage
print(calculate(2, 3, '+'))  # Output: 5
