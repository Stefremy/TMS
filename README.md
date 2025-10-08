# TMS
Calculadora

A simple command-line calculator that supports basic arithmetic operations.

## Features
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Error handling for division by zero
- Interactive mode

## Usage

### Interactive Mode
Run the calculator in interactive mode:
```bash
python3 calculator.py
```

Enter expressions in the format: `number operator number`
For example:
- `10 + 5`
- `20 - 8`
- `6 * 7`
- `15 / 3`

Type `quit` to exit.

### Using Functions in Code
```python
from calculator import add, subtract, multiply, divide

result = add(5, 3)        # Returns 8
result = subtract(10, 4)  # Returns 6
result = multiply(6, 7)   # Returns 42
result = divide(15, 3)    # Returns 5.0
```

## Testing
Run the test suite:
```bash
python3 test_calculator.py
```
