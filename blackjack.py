import cards
import random

"""
    Blackjack by Wes Leonard @dougienmesnuggy on Twitter. 
    
    This is a simple Python Blackjack game that uses the cards library that I
    created for various card games.
    
"""

class Player():
    def __init__(self, name, bankroll, hand, bet):
        self.player_name = name
        self.player_money = bankroll
        self.player_hand = hand
        self.player_bet = bet
        
    
    def draw_card(self, deck):
        self.player_hand.append(deck.deal_card())

        
def get_player_bet(p):
    bet_amount = int(input(f'{p.player_name} - Enter bet amount ($1-500): '))
    if bet_amount not in range (1, 501):
        print('Illegal bet. Try again')
        get_player_bet(p)
    else:
        return bet_amount
    
    
def get_num_players():
    num = int(input('Number of Players? (1-4): '))
    if num not in range(1,5):
        print('Invalid entry. Try again.')
        get_num_players()
    else:
        return num    
    
    
def print_player_hands(p):
    """
    Player 1 (bet): XX, XX (value)
    Player 2 (bet): XX, XX (value)
    Player 3 (bet): XX, XX (value)
    
    Player X Turn:
    Bet:
    Current Hand:
    (H)it, (S)tand, (D)ouble Down, Sur(r)ender
    """
    p_name = p.player_name
    p_bet = p.player_bet
    p_hand = []
    for c in p.player_hand:
        p_hand.append(f'{c.rank} {c.suit}')
    p_hand_value = 0
    print(f'{p_name} (${p_bet}): {p_hand} ({p_hand_value})')
    

def main():
    # Initialize round                
    blackjack_deck = cards.Deck()
    all_players = []
    num_players = get_num_players()

    #create appropriate amount of players.   
    for i in range(num_players):
        name = "PLAYER " + str(i + 1)
        new_player = Player(name, 5000, [], 0)
        all_players.append(new_player)
        
    # dealer will always be last player in the list (num_players + 1)
    new_player = Player("DEALER", 999999, [], 0)
    all_players.append(new_player)
    
    #blackjack_card = cards.Card("","")

    # Main game loop
    while True:
        # Get a bet from each player (except Dealer)
        for player in all_players[:-1]:
            # if we have money, set player bet, reduce player bankroll
            if player.player_money > 0:
                player.player_bet = int(get_player_bet(player))
                # IF player has money, but not enough to cover bet, it will adjust bet to remaining money
                if player.player_bet > int(player.player_money):
                    player.player_bet = int(player.player_money)
                player.player_money -= player.player_bet

       
        # Deal 2 cards to each player & dealer
        for player in all_players:
            player.draw_card(blackjack_deck)
            
        for player in all_players:
            player.draw_card(blackjack_deck)
        
        # Determine value of starting hand to show player
        
        
        # Need to display the hands in a pleasing manner
        for player in all_players:
            print_player_hands(player)

        # Will implement splitting later
         
        # Starting at player 1, get player action until they stand or bust
        # if hit, draw card and valuate hand. 
        # if bust, go to next player
        # if not bust go back to beginning of player loop with updated hand
        # continue loop for each player. Then do dealer with qualifying conditions like in casinos
        
        # determine winners
        
        # pay winners
        
        # repeat until game quit.
        

if __name__ == "__main__":
    main()

