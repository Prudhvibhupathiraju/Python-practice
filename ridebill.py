height = int(input("What is your height in cm?\n"))
if height > 120:
    age = int(input("what is your age?\n"))
    if age <= 18:
        print("Pay $7")
    else:
        print("Pay $12")
else:
    print("You canot ride")

