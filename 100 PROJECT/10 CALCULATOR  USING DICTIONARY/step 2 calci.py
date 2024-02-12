''' in this step asking again to perfrom calculation with that calculated answer with next new number'''

#calculator

#add
def add(n1,n2):
    return n1+n2
#subtraction
def subtract(n1,n2):
    return n1-n2
#multiplication
def multiply(n1,n2):
    return n1*n2
#division
def divide(n1,n2):
    return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1=float(input("what's your first number?  "))
num2=float(input("what's your second number?  "))

for symbol in operations:
    print(symbol)

operation_symbol=input("pic an operation from the above : ")
calculation_function=operations[operation_symbol]
first_answer=calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2}={first_answer}")

operation_symbol=input("pic another operation: ")
num3=float(input("what's your next number?  "))
calculation_function=operations[operation_symbol]
second_answer=calculation_function(first_answer,num3)

print(f"{first_answer} {operation_symbol} {num3}={second_answer}")