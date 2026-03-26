def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
    }
num1 = float(input("What's your first number?: "))
any_operation = True
while any_operation:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    num2 = float(input("What's your next number?: "))
    result = operations[operation](num1,num2)
    print(f"{num1} {operation} {num2}= {result}")
    to_continue = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : "))
    if to_continue == "y":
        num1 = result 
    else:
        any_operation = False 
         