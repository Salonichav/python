import random
import sys

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
          'J':10, 'Q':10, 'K':10, 'A':11} 

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in suits for r in ranks]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        if not self.cards:
            self.__init__() 
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def total(self):
        total = 0
        aces = 0
        for c in self.cards:
            total += values[c.rank]
            if c.rank == 'A':
                aces += 1
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total
    def __str__(self):
        return ', '.join(str(c) for c in self.cards)

def show_hands(player_hand, dealer_hand, hide_dealer_first=True):
    print("\nDealer's hand:")
    if hide_dealer_first:
        print(" <hidden card>,", dealer_hand.cards[1])
    else:
        print(" ", dealer_hand)
        print("  (Total:", dealer_hand.total(), ")")
    print("\nYour hand:")
    print(" ", player_hand)
    print("  (Total:", player_hand.total(), ")\n")

def player_turn(deck, player_hand):
    while True:
        if player_hand.total() == 21:
            print("Blackjack or 21! You can't hit anymore.")
            break
        move = input("Hit or Stand? (h/s): ").strip().lower()
        if move not in ('h','s','hit','stand'):
            print("Please enter 'h' or 's'.")
            continue
        if move.startswith('h'):
            card = deck.deal()
            player_hand.add_card(card)
            print("You drew:", card)
            print("Your total is", player_hand.total())
            if player_hand.total() > 21:
                print("You busted!")
                break
            elif player_hand.total() == 21:
                break
        else:
            print("You stand with", player_hand.total())
            break

def dealer_turn(deck, dealer_hand):

    print("\nDealer reveals cards:")
    print(" ", dealer_hand)
    while dealer_hand.total() < 17:
        card = deck.deal()
        dealer_hand.add_card(card)
        print("Dealer draws:", card, "-> total", dealer_hand.total())
    if dealer_hand.total() > 21:
        print("Dealer busts!")

def settle_bet(player_hand, dealer_hand, bet, balance):
    p = player_hand.total()
    d = dealer_hand.total()
    if p > 21:
        print("You lose the bet of", bet)
        return balance - bet
    if d > 21:
        print("Dealer busted — you win", bet)
        return balance + bet
    if p > d:
        print("You win! You gain", bet)
        return balance + bet
    if p < d:
        print("You lose. You lose", bet)
        return balance - bet
    print("Push (tie). Your bet is returned.")
    return balance

def play_round(deck, balance):
   
    while True:
        try:
            bet = int(input(f"You have {balance}. Enter bet (0 to quit round): "))
            if bet < 0 or bet > balance:
                print("Invalid bet (can't exceed your balance or be negative).")
            else:
                break
        except ValueError:
            print("Please enter a whole number for bet.")
    if bet == 0:
        return balance, False 

    player_hand = Hand()
    dealer_hand = Hand()
  
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_hands(player_hand, dealer_hand, hide_dealer_first=True)

    
    if player_hand.total() == 21 and dealer_hand.total() == 21:
        show_hands(player_hand, dealer_hand, hide_dealer_first=False)
        print("Both have Blackjack — push.")
        return balance, True
    if player_hand.total() == 21:
        show_hands(player_hand, dealer_hand, hide_dealer_first=False)
        print("Blackjack! You win 1.5x your bet.")
       
        balance += int(1.5 * bet)
        return balance, True

    player_turn(deck, player_hand)
    if player_hand.total() > 21:
        
        show_hands(player_hand, dealer_hand, hide_dealer_first=False)
        balance = settle_bet(player_hand, dealer_hand, bet, balance)
        return balance, True

  
    show_hands(player_hand, dealer_hand, hide_dealer_first=False)
    dealer_turn(deck, dealer_hand)

    
    balance = settle_bet(player_hand, dealer_hand, bet, balance)
    return balance, True

def main():
    print("Welcome to Blackjack!\nRules: Dealer hits < 17. Aces = 1 or 11. Blackjack pays 3:2.\n")
    deck = Deck()
    balance = 100  
    playing = True
    while playing and balance > 0:
        balance, want_continue = play_round(deck, balance)
        if not want_continue:
            print("You cashed out with", balance)
            break
        if balance <= 0:
            print("You're out of money — game over.")
            break
        again = input("Play another round? (y/n): ").strip().lower()
        if again not in ('y','yes'):
            playing = False
    print("Thanks for playing! Final balance:", balance)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")
        sys.exit(0)

