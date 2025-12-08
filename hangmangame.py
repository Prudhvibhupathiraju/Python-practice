import random
word_list = [
    "apple", "banana", "orange", "grape", "pear",
    "house", "table", "chair", "window", "door",
    "school", "pencil", "paper", "book", "teacher",
    "water", "river", "ocean", "mountain", "garden",
    "dog", "cat", "bird", "fish", "horse",
    "happy", "sad", "pretty", "funny", "strong",
    "green", "blue", "red", "yellow", "black",
    "music", "movie", "party", "family", "friend",
    "morning", "night", "sun", "moon", "star",
    "baby", "brother", "sister", "father", "mother",
    "car", "bus", "train", "street", "bridge"
]
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"
word = random.choice(word_list)
display = []
for i in word:
  display.append("_")
print(" ".join(display))
lives = 6
while lives>0:
  opt = str(input("Type a letter\n")).lower()
  if opt in word:
    for index, letter in enumerate(word):
      if opt == letter:
        display[index] = opt
  else:
    lives -= 1
    print(f"{RED}Wrong lost a life! Lives remaining {lives}{RESET}")
       
  print(f"{BLUE}Your lives left:{lives}{RESET}")  
  result = " ".join(display)  
  print(result)
  if "_" not in display:
    print(f"{GREEN}You Win{RESET}")    
    break
if lives ==0:
  print(f"{RED}Game over{RESET}")
  print(f"{YELLOW}Your word is {word}{RESET}")
    

