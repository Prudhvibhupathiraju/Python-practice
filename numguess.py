import random
print(r"""  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/      """)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
FIXED_NUM = random.randint(1, 100)
difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard':")).lower()
if difficulty == "easy":
    remaining_lives = 10
else:
    remaining_lives = 5
while remaining_lives > 0 :
    print(f"You have {remaining_lives} attempts remaining to guess the number.")
    guess_num = int(input("Make a guess:"))
    if guess_num > FIXED_NUM:
        print("Too high\nGuess Again")
        remaining_lives -= 1
    elif guess_num < FIXED_NUM:
        print("Too low\nGuess Again")
        remaining_lives -= 1
    else:
        print(f"You got it! The answer was {FIXED_NUM}.")
        break 
if remaining_lives == 0:
    print("You've run out of guesses.")

