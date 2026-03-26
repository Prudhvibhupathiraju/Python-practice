import random
print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/                
""")
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
player_cards = [random.choice(cards), random.choice(cards)]
print(f"Your cards :{player_cards}, current score :{sum(player_cards)}")
computer_cards = [random.choice(cards), random.choice(cards)]
print(f"Computer's first card {computer_cards[0]}")
get_card = True
while get_card :
    opt_card = str(input("Type 'y' to get another card, type 'n' to pass:")).lower()
    if opt_card == "y":
        player_cards.append(random.choice(cards))
        print(f"Your cards :{player_cards}, current score :{sum(player_cards)}")
        print(f"Computer's first card {computer_cards[0]}")
        while sum(player_cards) > 21 and 11 in player_cards:
            player_cards[player_cards.index(11)] = 1
        if sum(player_cards) > 21:
            print("You went over, You lose")
            get_card = False
    else:
        get_card = False
while sum(computer_cards) < 17:
    computer_cards.append(random.choice(cards))
    while sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards[computer_cards.index(11)] = 1  
print(f"Your final hand :{player_cards}, final score: {sum(player_cards)}")
print(f"Computer's final hand : {computer_cards}, final score: {sum(computer_cards)}")
if sum(computer_cards) > 21:
    print("Computer went over, You Win")
elif sum(player_cards) > sum(computer_cards):
    print("You win")
elif sum(computer_cards) > sum(player_cards):
    print("You lose")
else:
    print("Draw")   