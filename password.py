import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for a in range(0,nr_letters):
  print(random.choice(letters),end='')
for b in range(nr_symbols):
  print(random.choice(symbols),end='')
for c in range(nr_numbers):
  print(random.choice(numbers),end='')
password=[]
for a in range(0,nr_letters):
  password+=random.choice(letters)
print(password,type(password))
for b in range(nr_symbols):
  password+=random.choice(symbols)
for c in range(nr_numbers):
  password+=random.choice(numbers)
random.shuffle(password)
print(password)
final_p=""
for char in password:
  final_p=char+final_p
print(final_p)
