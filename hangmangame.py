import random
word_list = [ "aardvark", "baboon", "camel", "python", "computer", "science", "elephant", "airplane",
    "notebook", "penguin", "mountain", "ocean", "rainbow",
    "sandwich", "giraffe", "volcano", "library", "puzzle",
    "diamond", "chocolate", "calendar", "backpack", "tornado",
    "castle", "battery", "adventure", "festival", "galaxy",
    "kangaroo", "lighthouse", "microscope", "parrot", "treasure", "adventure", "balloon", "bicycle", "crocodile", "dinosaur",
    "electric", "fireworks", "galaxy", "harmonica", "iguana",
    "jungle", "keyboard", "lantern", "magnet", "nectarine",
    "octopus", "pirate", "quicksand", "rocket", "satellite",
    "telescope", "umbrella", "volcano", "whistle", "xylophone",
    "yogurt", "zeppelin", "astronaut", "bamboo", "caterpillar",
    "dragon", "emerald", "forest", "glacier", "horizon",
    "island", "jigsaw", "koala", "labyrinth", "meteor",
    "nebula", "orchard", "peacock", "quiver", "rainforest",
    "sapphire", "treasure", "unicorn", "voyage", "wizard" ]
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
    print(f"Wrong lost a life! Lives remaining {lives}")
       
  print(f"Your lives left:{lives}")  
  print(" ".join(display))
  if "_" not in display:
    print("You Win")    
    break
if lives ==0:
  print("Game over")
  print(f"Your word is {word}")
    

