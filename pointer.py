num1 = 11
num2 = 11

print("Before num2 value is updated")
print(f"num1 = {num1}")
print(f"num2 = {num2}")
print("\nnum1 points to ", id(num1))
print("num2 points to ", id(num2))
num2 = 22

print("After num2 value is updated")
print(f"num1 = {num1}")
print(f"num2 = {num2}")
print("\nnum1 points to ", id(num1))
print("num2 points to ", id(num2))

dict1 = { 'value' : 22 }
dict2 = dict1

print("Before dict2 value is updated")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print("dict1 points to ", id(dict1))
print("dict2 points to ", id(dict2))

dict2['value'] = 11

print("After dict2 value is updated")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print("dict1 points to ", id(dict1))
print("dict2 points to ", id(dict2))
