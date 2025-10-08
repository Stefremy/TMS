#!/usr/bin/env python3
"""
Simple Calculator
Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Main function to run the calculator in interactive mode."""
    print("=== Calculator ===")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")
    print()
    
    while True:
        try:
            user_input = input("Enter expression (e.g., 5 + 3): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Parse the input
            parts = user_input.split()
            if len(parts) != 3:
                print("Error: Please use format: number operator number (e.g., 5 + 3)")
                continue
            
            num1_str, operator, num2_str = parts
            
            # Convert to numbers
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
            except ValueError:
                print("Error: Invalid numbers. Please enter valid numbers.")
                continue
            
            # Perform calculation
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                try:
                    result = divide(num1, num2)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
            else:
                print(f"Error: Unknown operator '{operator}'. Use +, -, *, or /")
                continue
            
            print(f"Result: {result}")
            print()
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue


if __name__ == "__main__":
    main()
