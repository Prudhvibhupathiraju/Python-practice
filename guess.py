import random

word_list = [ "aardvark", "baboon", "camel" ]
word = random.choice(word_list)
print(word)
opt = str(input("Type a letter\n")).lower()

for letter in word:
  print(letter[word])
 
  
