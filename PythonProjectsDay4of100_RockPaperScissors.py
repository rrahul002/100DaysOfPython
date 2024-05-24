rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


import random

userchoice = input("Rock, Paper, or Scissor? Type 0 for Rock, 1 for Paper, or 2 for Scissor.")

userchoice = int(userchoice)

if userchoice == 0:
  theirchoice = "Rock"
  image0 = rock
elif userchoice == 1:
  theirchoice = "Paper"
  image0 = paper
elif userchoice == 2:
  theirchoice = "Scissor"
  image0 = scissors

computerchoice = random.randint(0,2)

if computerchoice == 0:
  thechoice = "Rock"
  image1 = rock
elif computerchoice == 1:
  thechoice = "Paper"
  image1 = paper
elif computerchoice == 2:
  thechoice = "Scissor"
  image1 = scissors

if userchoice == 0 and computerchoice == 0:
  decision = "tied"
elif userchoice == 0 and computerchoice == 1:
  decision = "LOSE"
elif userchoice == 0 and computerchoice == 2:
  decision = "WIN"
elif userchoice == 1 and computerchoice == 0:
  decision = "WIN"
elif userchoice == 1 and computerchoice == 1:
  decision = "tied"
elif userchoice == 1 and computerchoice == 2:
  decision = "LOSE"
elif userchoice == 2 and computerchoice == 0:
  decision = "LOSE"
elif userchoice == 2 and computerchoice == 1:
  decision = "WIN"
elif userchoice == 2 and computerchoice == 2:
  decision = "tied"

print("You chose " + theirchoice + image0 + " and the computer chose " + thechoice + image1)

print("You " + decision)
