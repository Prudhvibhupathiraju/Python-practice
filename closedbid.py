condition = True
bid_dict = {}
while condition == True:
  print("\n" * 100)
  name = str(input("what is your name\n"))
  bid = int(input("what is your bid amount\n"))
  bid_dict[name] = bid
  opt = str(input("Is there are other bidders yes or no\n")).lower()
  if opt == "no":
    print("\n" * 100)
    condition = False
print("\n" * 100)
max_bid = 0
max_bidder = None
for key, value in bid_dict.items():
  if value > max_bid:
    max_bid = value
    max_bidder = key
print(f"Winner is {max_bidder} with bid {max_bid}")    
    
  
