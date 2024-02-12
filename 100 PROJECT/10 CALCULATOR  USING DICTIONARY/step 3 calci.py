''' in this step asking again to continue ur MANY calculation '''


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

def calculator():

    num1=float(input("what's your first number?  "))

    for symbol in operations:
            print(symbol)
    should_continue=True

    while  should_continue:

        operation_symbol=input("pic an operation  : ")
        num2=float(input("what's your second number?  "))
        calculation_function=operations[operation_symbol]
        
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2}={answer}")

        #if input(f"Type 'y' to continue calculating with {answer} , or type 'n' to exit.:  ")=='y':
        #num1=answer
        #else:
        #    should_continue=False'''
        
        ''' sad part is here is that we cannot do fresh calculation . so for this u can use concept of RECURSION'''
        
        if input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation.:  ")=='y':
         num1=answer
        else:
            should_continue=False
            calculator()



calculator()