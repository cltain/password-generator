#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Order not randomised:
password = ""
for char in range(1,nr_letters + 1):
  randletter = random.choice(letters)
  password += randletter
for char in range(1, nr_symbols + 1):
  randsym = random.choice(symbols)
  password += randsym
for char in range(1, nr_numbers + 1):
  randnum = random.choice(numbers)
  password += randnum
print(f"Non-randomized password: {password}")

#Order of characters randomised:
password = []
for char in range(1,nr_letters + 1):
  randletter = random.choice(letters)
  password += randletter
for char in range(1, nr_symbols + 1):
  randsym = random.choice(symbols)
  password += randsym
for char in range(1, nr_numbers + 1):
  randnum = random.choice(numbers)
  password += randnum
random.shuffle(password)
password2 = ""
for i in password:
  password2 += i
print(f"Randomized password: {password2}")
