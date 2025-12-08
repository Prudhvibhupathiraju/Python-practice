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
    print(f"\033[91mWrong lost a life! Lives remaining {lives}")
       
  print(f"\033[94mYour lives left:{lives}")  
  result = " ".join(display)  
  print(result)
  if "_" not in display:
    print("\033[92mYou Win")    
    break
if lives ==0:
  print("\033[91mGame over")
  print(f"\033[94mYour word is {word}")
    

