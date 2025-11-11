height = int(input("What is your height in cm?\n"))
if height > 120:
    age = int(input("what is your age?\n"))
    bill = 0
    if age < 12:
        print("Pay $5")
        bill = 5
    elif age >= 12 and age <= 18:
        bill = 7
        print("Pay $7")
    elif age > 18 and age < 45 :
        bill = 12
        print("Pay $12")
    elif age >= 45 and  age <= 55:
        bill = 0
    pic = input("Do you want to take a pic? Y or N")
    if pic == "Y":
         bill += 3
    print(f"The bill amount is {bill}")

else:
    print("You canot ride")

