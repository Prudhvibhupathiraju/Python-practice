import random

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '?']

num_letters = int(input("Enter the num of letters you want to use\n"))
num_numbers = int(input("Enter the num of numbers you want to use\n"))
num_symbols = int(input("Enter the num of symbols you want to use\n"))

password=[]

for letter in range(num_letters):
    password.append(random.choice(letters))

for number in range(num_numbers):
    password.append(random.choice(numbers))

for symbol in range(num_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
result = ""
for char in password:
    result += char

print(f"Yor password is : {result}")