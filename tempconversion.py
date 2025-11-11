print("welcome to temperature conversion\nDisplay Menu:\n1. Celsius → Fahrenheit\n2. Fahrenheit → Celsius")
choice = int(input("Enter your choice(1 or 2)"))
if choice == 1:
    c = float(input("Enter the temperature in C\n"))
    f = 0
    f = round((float(c * 9/5) + 32), 2)
    print(f"{c}C = {f}F")
elif choice == 2:
    f = float(input("Enter the temperature in F\n"))  
    c = 0
    c = round((f - 32) * 5/9, 2)
    print(f"{f}F = {c}C")
else:
    print("Invalid Input")