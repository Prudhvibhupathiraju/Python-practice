size= input("Which size of pizza do you want S M L\n")
pepparoni = input("Do you want pepparoni Y or N\n")
cheese = input("Do you want chesse Y or N\n")
if size == "S":
    bill = 15
    if pepparoni == "Y":
        bill += 2
    if cheese == "Y":
        bill += 1
    print(f"your bill is ${bill}")    
elif size == "M":
    bill = 20
    if pepparoni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
    print(f"your bill is ${bill}")     
elif size =="L":
    bill = 25
    if pepparoni == "Y":
        bill += 3
    if cheese == "Y":
        bill += 1
    print(f"your bill is ${bill}")     
else:
    print("Wrong Input")

