# This module contains all the functions, data and classes related to cards and the dealing of the deck.

# requirements
from random import shuffle
import logging
import threading
# all possible cards
allcardnums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
allcardtypes = ["♠", "♣", "♦", "♥"]

# logger
log = logging.getLogger("Deck Manager")

# card class - this allows me to make the cards python objects, which makes them easier to compare and reduces errors
class card:

	def __init__(self, card_type, card_num):
		self.type = card_type
		self.number = card_num

	def __str__(self):
		return f"{self.type} {self.number}"

	def __eq__(self, other):
		if self.__class__ != other.__class__:
			return NotImplementedError
		return (self.number == other.number)

# custom error for if there are too many decks
class TooManyDecksError(Exception):
    "Too many decks were requested."
    pass

# generates the deck
def newdeck(num: int):
	global log
	log.info("Generating new deck...")
	if type(num) != int:
		log.error("TypeError: newdeck function was given a non-integer, but requires an integer to prevent errors.")
		raise TypeError("newdeck function was given a non-integer, but requires an integer to prevent errors.")
		return None
	if int(num) > 8 or int(num) <= 0:
		return TooManyDecksError
	else:
		num = int(num)
		global allcardtypes, allcardnums
		deck = []
		for _ in range(num):
			for x in allcardtypes:
				for y in allcardnums:
					deck.append(card(x, y))
		shuffle(deck)
		return deck