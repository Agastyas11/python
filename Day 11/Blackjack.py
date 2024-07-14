import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)

user_cards = []
computer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

def calculate_score(numbers):
    number = sum(numbers)
    if number == 21: 
     return 0
    elif 11 in numbers and number > 21:
      numbers.remove(11)
      numbers.append(1)
    else:
     return number
GameEnd = False
WannaPlay = input("Do you want to play a game of Blackjack? Type 'y' or 'n'?\n")
if WannaPlay == "y":
  print(logo)
  print(f"  Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
  print(f"  Computer's first card: {computer_cards[0]}")
  PassOrNot = input("Type 'y' to get another card, type 'n' to pass: ")
  while GameEnd == False:
    if PassOrNot == "y":
      user_cards.append(deal_card())
      print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
      print(f"Computer's first card: {computer_cards[0]}")
      if sum(user_cards) > 21:
        print("You went over. You lose :(")
        GameEnd = True
      elif sum(user_cards) == 0 or sum(user_cards) == 21:
        print("BLACKJACK! you win! :)")
        GameEnd = True
    elif PassOrNot == "n":
      print(f"Your final hand: {user_cards}, current score: {sum(user_cards)}")
      abovefifteen = False
      while abovefifteen == False:
        if sum(computer_cards) <= 15:
          computer_cards.append(deal_card())
        else:
          abovefifteen = True
      print(f"Computer's final hand {computer_cards}, final score: {sum(computer_cards)}")
      if sum(computer_cards) > sum(user_cards) and sum(computer_cards) <= 21:
        print("Computer is closer to 21, You lose :(")
        GameEnd = True
      elif sum(computer_cards) > 21:
        print("Computer went over 21, You win! :)")
        GameEnd = True
      elif sum(computer_cards) < sum(user_cards):
        print("You are closer to 21, You win! :)")
        GameEnd = True
else:
  quit()



