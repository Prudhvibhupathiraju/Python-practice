import random

word_list = [ "aardvark", "baboon", "camel" ]
word = random.choice(word_list)
print(word)

display = []

for i in word:
  display.append("_")
print(" ".join(display))
while ("".join(display)) != word:
  opt = str(input("Type a letter\n")).lower()
  remaining = []
  for index, letter in enumerate(word):
    if opt == letter:
      remaining[index] = opt
    
  print(" ".join(remaining))
