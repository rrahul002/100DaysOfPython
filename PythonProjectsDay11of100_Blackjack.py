import random

print("Welcome to Blackjack!")
cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3',
    '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5',
    '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7',
    '8', '9', '10', 'J', 'Q', 'K', 'A'
]


def card_value(card):
  if card == 'J' or card == 'Q' or card == 'K':
    return 10
  elif card == 'A':
    return 11
  else:
    return int(card)


def deal_card():
  return random.choice(cards)


def calculate_score(hand):
  score = sum(card_value(card) for card in hand)
  if score > 21 and 'A' in hand:
    hand.remove('A')
    hand.append('1')
    score = sum(card_value(card) for card in hand)
  return score


def play_game():
  player_hand = [deal_card(), deal_card()]
  dealer_hand = [deal_card(), deal_card()]
  while True:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print(f"Your hand: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")
    if player_score == 21:
      print("Blackjack! You win!")
      break
    elif player_score > 21:
      print("Bust! You lose.")
      break
    else:
      choice = input("Do you want to hit or stand? ")
      if choice.lower() == 'hit':
        player_hand.append(deal_card())
      elif choice.lower() == 'stand':
        while dealer_score < 17:
          dealer_hand.append(deal_card())
          dealer_score = calculate_score(dealer_hand)
        if dealer_score > 21:
          print(f"Dealer's hand: {dealer_hand}, final score: {dealer_score}")
          print("Dealer busts! You win!")
        elif dealer_score > player_score:
          print(f"Dealer's hand: {dealer_hand}, final score: {dealer_score}")
          print("Dealer wins!")
        elif dealer_score < player_score:
          print(f"Dealer's hand: {dealer_hand}, final score: {dealer_score}")
          print("You win!")
        else:
          print(f"Dealer's hand: {dealer_hand}, final score: {dealer_score}")
          print("It's a tie!")
        break


play_game()
