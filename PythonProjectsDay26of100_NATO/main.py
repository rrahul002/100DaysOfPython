import pandas

user_name = input("Enter Name: ").upper()

file = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in file.iterrows()}

name = [alphabet[letter] for letter in user_name]

print(name)