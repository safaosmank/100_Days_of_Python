#calculator
from calc_art import logo

#Add
def add(n1 , n2):
  return n1 + n2

#subtraction

def subtract(n1, n2):
  return n1 - n2

#multiplication

def multiply(n1 , n2):
  return n1 * n2

#divide 

def divide(n1 , n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  continue_calculation= True
 
  while continue_calculation:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
 

