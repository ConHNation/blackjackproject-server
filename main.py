# requirements
from random import choice, randint

#game variables
deck = []

# game functions
def start_deck():
    global deck
    card_type = ["♠", "♣", "⬩", "♥"]
    card_nums = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    seleted_card 

def shuffle_deck():
    card_type = ["♠", "♣", "⬩", "♥"]
    card_nums = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    print(card_nums)
    return choice(card_type), choice(card_nums)


# game code
card = random_card()
print(f"Your Cards: {card[0]} {card[1]}")
#if card.
card = random_card()
print(f"Dealer Cards: {card[0]} {card[1]}")