import random

word_list = [ "aardvark", "baboon", "camel" ]
word = random.choice(word_list)
print(word)

display = []

for letter in word:
  display.append("_")
print(" ".join(display))

opt = str(input("Type a letter\n")).lower()
 
for i in word:
  if opt == letter:
    display[i] = word[i]

print(" ".join(display))
