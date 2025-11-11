print("welcome to the simple calculator")
print("Please find the menu operations")
print("Display Menu:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
operation = int(input("Choose the above operation(1,2,3,4)"))
a = float(input("Enter the first number\n"))
b = float(input("Enter the second number\n"))
result = 0
if operation == 1:
    result = a + b
    print(f"{result}")
elif operation == 2:
    result = a - b
    print(f"{result}")
elif operation == 3:
    result = a * b
    print(f"{result}")
elif operation == 4:
    result == a / b 
    print(f"{result}")   
else:
    print("Invalid option")    


