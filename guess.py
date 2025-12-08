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
  if opt in word:
    for index, letter in enumerate(word):
      if opt == letter:
        display[index] = opt
   else:
     lives -= 1
     print(f"Wrong lost a life! Lives remaining {lives}")  
    
  print(f"Your lives left:{lives}")  
  print(" ".join(display))
  if "_" not in display:
    print("You Win")
if lives ==0:
  print("Game over")
  print(f"Your word is {word}")
    

