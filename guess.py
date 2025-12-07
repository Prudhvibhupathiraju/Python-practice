import random

word_list = [ "aardvark", "baboon", "camel" ]
word = random.choice(words)

opt = int(input("Type a letter\n"))

for letter in word:
  if opt == letter:
    print("Correct")
  else:
    print("Not Correct")
  
