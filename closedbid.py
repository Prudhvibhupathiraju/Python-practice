Condition = True:
bid_dict = {}
while condition = True:
  name = input(str("what is your name\n"))
  bid = input(int("what is your bid amount\n"))
  bid_dict[name] = bid
  opt = input(str("Is there are other bidders yes or no\n")).lower()
  if opt == "no":
    print("\n" * 100)
    condition = False
max_bid = 0
max_bidder = None
for key, value in bid_dict.items():
  if value > max_bid:
    max_bid = value
    max_bidder = key
print(f"Winner is {max_bidder} with bid {max_bid}")    
    
  
