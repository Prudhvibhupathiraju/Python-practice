alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def encrypt(text, shift):
  encrypt_message = ""
  for letter in text.lower():
    index = alphabet.index(letter)
    new_index = (index + shift) % 26
    encrypt_message += alphabet[new_index]  
  print(encrypt_message)
def decrypt(text, shift):
  decrypt_message = ""
  for letter in text.lower():
    index = alphabet.index(letter)
    new_index = (index - shift) % 26
    decrypt_message += alphabet[new_index]  
  print(decrypt_message)
While condition is True
    direction = str(input("Type 'encode' to encrypt or 'decode' to decrypy\n")).lower()
    text = input("Type your message\n") 
    shift = int(input("Type the shift number\n"))
    
    if direction == "encode":
      encrypt(text, shift)
    if direction == "decode":
      decrypt(text, shift)
    opt = str(input("Type yes to go back or no to stop\n"))
    if opt is "no":
        condition is False
    else:
        condition is True
  
  
  
  
