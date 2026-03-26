import random
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
player_cards = [random.choice(cards), random.choice(cards)]
print(f"Your cards :{player_cards}, current score :{sum(player_cards)}")
computer_cards = [random.choice(cards), random.choice(cards)]
print(f"Computer's first card {computer_cards[0]}")
get_card = True
while get_card:
    opt_card = str(input("Type 'y' to get another card, type 'n' to pass:")).lower
    player_cards.append(random.choice(cards))
    print(f"Your cards :{player_cards}, current score :{sum(player_cards)}")
    print(f"Computer's first card {computer_cards[0]}")
    if opt_card == "y":
        get_card = True
    else:
        get_card = False    


