import random
from replit import clear
from cardsart import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calc_score(cards):

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, comp_score):
  if user_score > 21 and comp_score > 21:
    return "You went over. You lose "


  if user_score == comp_score:
    return "Draw "
  elif comp_score == 0:
    return "Lose, opponent has Blackjack "
  elif user_score == 0:
    return "Win with a Blackjack "
  elif user_score > 21:
    return "You went over. You lose "
  elif comp_score > 21:
    return "Opponent went over. You win"
  elif user_score > comp_score:
    return "You win "
  else:
    return "You lose "

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not game_over:
    user_score = calc_score(user_cards)
    comp_score = calc_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or comp_score == 0 or user_score > 21:
      game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  while comp_score != 0 and comp_score < 17:
    computer_cards.append(deal_card())
    comp_score = calc_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {comp_score}")
  print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()