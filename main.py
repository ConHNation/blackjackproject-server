# Blackjack - Server (Back-end) Program
# CSP Final Project
# Made by Connor Hayden, Dylan Lovell, Mateus and all the other nerds idfk

# dependencies
from deck import card
import deck
import balance
import packet
import threading
import logging

# initialize logging
log = logging.getLogger("main")
log.info("Starting game...")