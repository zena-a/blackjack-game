############### Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
################################################################
#Built using while loops, lists and functions with outputs.
import random
from ascii_art import logo
from clearscreen import clear

#List containing number values of a deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Returns a random card from the deck"""
  random_card = random.choice(cards)
  return random_card

def calculate_score(card_list):
  """Returns the score of the cards in the player's hand"""
  card_score = sum(card_list)
  #Either computer or user gets blackjack (hand with ace and 10)
  if card_score == 21 and len(card_list) == 2:
    return 0
  if 11 in card_list and card_score > 21:
    card_list.remove(11)
    card_list.append(1)
  
  return card_score

def compare(user_score, computer_score):
  """Lets user know whether they've won, lost or it's a draw"""
  if computer_score == user_score:
    print("It's a draw")
  elif computer_score == 0:
    print("You lose")
  elif user_score == 0:
    print("You win.")
  elif user_score > 21:
    print("You lose.")
  elif computer_score > 21:
    print("You win")
  elif user_score > computer_score:
    print("You win")
  else:
    print("You lose")

def play_game():
  """Runs the blackjack game with the final scores printed out"""
  user_cards = []
  computer_cards = []
  game_over = False

  print(logo)

  #Deals two cards to start of the player's hand
  for dealing in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Allows user to hit or stand and tracks players' score
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")
      if hit_or_stand == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  #Allows computer to take more cards once the score < 17
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  #Prints final scores for players
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  #Prints whether user one or lost using compare() function
  compare(user_score, computer_score)

#Main program 
#Loops through game once player decides to play again 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()