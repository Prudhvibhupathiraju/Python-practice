import random

word_list = [ "aardvark", "baboon", "camel" ]
word = random.choice(word_list)
print(word)

display = []

for i in word:
  display.append("_")
print(" ".join(display))

opt = str(input("Type a letter\n")).lower()
remaining = []
for letter in word:
  if opt == letter:
    remaining[letter] = opt
  else:
    remaining[letter] = "_"

print(" ".join(remaining))
