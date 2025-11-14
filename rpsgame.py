import random
options = ["Rock","Paper", "Scissors"]
manual = int(input("Please select the options\n1.Rock\n2.Paper\n3.Scisscors\n"))
if manual >= 1 and manual <= 3:
    print("You chose --->", options[manual - 1])
    auto_choise = options[random.randint(0, 2)]
    print("Computer chose --->", auto_choise)
    if options[manual - 1] == "Rock" and auto_choise == "Scissors":
        print("You Won")
    elif options[manual - 1] == "Scissors" and auto_choise == "Paper": 
        print("You Won")
    elif options[manual - 1] == "Paper" and auto_choise == "Rock": 
        print("You Won")
    elif options[manual - 1] == auto_choise:
        print("Draw")  
    else:
        print("You Lost")    
else:
    print("Invalid Option")
    
