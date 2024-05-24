import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if (difficulty == "easy"):
  attempts = 10
else:
  attempts = 5

number = random.randint(1, 100)

attempts_left = attempts

for x in range(attempts):
  print("You have " + str(attempts_left) +
        " attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if (guess == number):
    print("You got it! The answer was " + str(number) + ".")
    print("You got it in " + str(x) + " guesses.")
    break
  elif (guess > number):
    print("Too high.")
  elif (guess < number):
    print("Too low.")

  attempts_left = attempts_left - 1
  if (attempts_left == 0):
    print("You've run out of guesses, you lose.")
    break
