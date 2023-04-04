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
        


def main():
    # Initialize round                
    blackjack_deck = cards.Deck()
    dealer = Player("DEALER", 9999999)
    player1 = Player("PLAYER 1", "5000")
    blackjack_card = cards.Card("","")



    # Main game loop 

    while True:
        blackjack_deck.reset_deck()
        blackjack_deck.shuffle()
        dealer_hand, player1_hand = [], []

        # Need to accept bets
        
        
        # Deal initial hand
        player1_hand.append(blackjack_deck.deal_card())
        dealer_hand.append(blackjack_deck.deal_card())
        player1_hand.append(blackjack_deck.deal_card())
        dealer_hand.append(blackjack_deck.deal_card())
        
        # Testing to print out player and dealer hands. Need to find a 
        # better way to display the hands on screen.
        for blackjack_card in player1_hand:
            blackjack_card.print_card()

        for blackjack_card in dealer_hand:
            blackjack_card.print_card()
            
    # This is currently an infinite loop that just keeps dealing 2 cards to dealer and player 1


if __name__ == "__main__":
    main()

