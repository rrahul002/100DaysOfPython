import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']






print("Welcome to the Password Generator!")
numLetters = int(input("How many letters would you like in your password?"))
numSymbols = int(input("How many symbols would like in your password?"))
numNumbers = int(input("And how many numbers would you like in your password?"))

PasswordList = []

for n in range(1, numLetters + 1):
  PasswordList.append(random.choice(letters))
for n in range(1, numSymbols + 1):
  PasswordList.append(random.choice(symbols))
for n in range(1, numNumbers + 1):
  PasswordList.append(random.choice(numbers))

random.shuffle(PasswordList)
 
#print(PasswordList)

password = ""
for n in PasswordList:
  password += n

print(f"Your new password is: {password}")
