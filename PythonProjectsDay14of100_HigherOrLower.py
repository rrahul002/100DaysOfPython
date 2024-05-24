import random
print("Welcome to Higher or Lower!")

data= [
  
    {
        "name": "Elon Musk",
        "followers": 57900000
    },
    {
        "name": "Barack Obama",
        "followers": 130000000
    },
    {
        "name": "Oprah Winfrey",
        "followers": 42900000
    },
    {
        "name": "Ellen DeGeneres",
        "followers": 80000000
    },
    {
        "name": "Cristiano Ronaldo",
        "followers": 500000000
    },
    {
        "name": "Beyoncé",
        "followers": 170000000
    },
    {
        "name": "Kylie Jenner",
        "followers": 305000000
    },
    {
        "name": "Donald Trump",
        "followers": 89800000
    },
    {
        "name": "Taylor Swift",
        "followers": 154000000
    },
    {
        "name": "Justin Bieber",
        "followers": 179000000
    },
    {
        "name": "Kim Kardashian",
        "followers": 392000000
    },
    {
        "name": "Katy Perry",
        "followers": 118000000
    },
    {
        "name": "Drake",
        "followers": 85000000
    },
    {
        "name": "Neymar Jr",
        "followers": 150000000
    },
    {
        "name": "Ariana Grande",
        "followers": 240000000
    },
    {
        "name": "Shakira",
        "followers": 158000000
    },
    {
        "name": "Rihanna",
        "followers": 100000000
    },
    {
        "name": "The Rock",
        "followers": 278000000
    },
    {
        "name": "Kevin Hart",
        "followers": 98000000
    },
    {
        "name": "Serena Williams",
        "followers": 15000000
    }
]

def random_data():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  followers = account["followers"]
  return f"{name}"

def format_data2(account):
  name = account["name"]
  followers = account["followers"]
  return f"{name} has {followers} followers"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  score = 0
  continue_game = True
  account_a = random_data()
  account_b = random_data()
  while continue_game:
    account_a = account_b
    account_b = random_data()
    while account_a == account_b:
      account_b = random_data()
    print(f"Compare A: {format_data2(account_a)}")
    print(f"Compare B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_followers = account_a["followers"]
    b_followers = account_b["followers"]
    is_correct = check_answer(guess, a_followers, b_followers)
    if is_correct:
      score += 1
      print(f"You're right! {format_data2(account_a)} and {format_data2(account_b)}. Current score: {score}.")
    else:
      continue_game = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
