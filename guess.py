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
    remaining.append(opt)
  else:
    remaining.append("_")

print(" ".join(remaining))
