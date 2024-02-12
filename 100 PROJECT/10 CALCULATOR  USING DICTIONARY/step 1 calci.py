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
num2=float(input("what's your first number?  "))

for symbol in operations:
    print(symbol)

operation_symbol=input("pic an operation from the above : ")
calculation_function=operations[operation_symbol]
answer=calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2}={answer}")

