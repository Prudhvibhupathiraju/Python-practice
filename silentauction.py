print("Welcome to silent auction")
silent_auction = {}
any_other_bidders = True
while any_other_bidders:
    name = str(input("What is your name\n"))
    bid_amount = float(input("what is amount you are going to bid $\n"))
    silent_auction[name] = bid_amount
    other_bidders = str(input("Any other bidders 'Yes' or 'No'\n"))
    if other_bidders.lower() == "yes":
        any_other_bidders = True
        print("\n" * 100)
    else:
        any_other_bidders = False
highest_bid = 0
highest_bidder = ""        
for key in silent_auction:
    if silent_auction[key] > highest_bid:
        highest_bid = silent_auction[key]
        highest_bidder = key
print("\n" * 100)        
print(f"{highest_bidder} won the silent auction with bid amount {highest_bid}")        
                