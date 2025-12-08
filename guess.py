import random
word_list = [ "aardvark", "baboon", "camel" ]
word = random.choice(word_list)
print(word)
display = []
for i in word:
  display.append("_")
print(" ".join(display))
lives = 6
while lives>0:
  opt = str(input("Type a letter\n")).lower()
  for index, letter in enumerate(word):
    if opt == letter:
      display[index] = opt
    elif opt != letter:
      lives -= 1
      if lives = 0:
      print("Game Over!")
    print(f"Your lives left:{lives}")  
  print(" ".join(display))
