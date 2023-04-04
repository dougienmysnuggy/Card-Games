import cards
import random

"""
    Blackjack by Wes Leonard @dougienmesnuggy on Twitter. 
    
    This is a simple Python Blackjack game that uses the cards library that I
    created for various card games.
    
"""

class Player():
    def __init__(self, name, bankroll):
        self.player_name = name
        self.player_money = bankroll
        
                
blackjack_deck = cards.Deck()
blackjack_deck.shuffle()
dealer = Player("DEALER", 9999999)
player1 = Player("PLAYER 1", "5000")
dealer_hand, player_hand = []




