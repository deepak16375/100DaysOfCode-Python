# Importing necessary modules for the calculator program
from replit import clear
from art import logo

# Function to add two numbers
def add(n1, n2):
  return n1 + n2

# Function to subtract two numbers
def subtract(n1, n2):
  return n1 - n2

# Function to multiply two numbers
def multiply(n1, n2):
  return n1 * n2

# Function to divide two numbers
def divide(n1, n2):
  return n1 / n2

# Dictionary to map symbols to corresponding operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Main calculator function
def calculator():
  print(logo)

  # Taking the first number as input
  num1 = float(input("What's the first number?: "))
  
  # Displaying available operation symbols
  for symbol in operations:
    print(symbol)
  
  # Flag to continue or start a new calculation
  should_continue = True
  
  while should_continue:
    # Taking operation symbol as input
    operation_symbol = input("Pick an operation: ")
    
    # Taking the next number as input
    num2 = float(input("What's the next number?: "))
    
    # Retrieving the corresponding function based on the chosen operation
    calculation_function = operations[operation_symbol]
    
    # Calculating and displaying the result
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # Asking the user whether to continue with the result or start a new calculation
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

# Initial call to start the calculator
calculator()
