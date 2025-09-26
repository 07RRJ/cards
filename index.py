from dataclasses import dataclass

@dataclass
class Card:
    suit: str
    value: str

    def __str__(self):
        return f"{self.suit} {self.value}"
    
    def __repr__(self):
        return f"{self.suit} {self.value}"

class Deck:
    def __init__(self, cards=None): 
        if cards is None:
            cards = []
        self.cards = cards
        
    def show_all(self):
        for card in self.cards:
            if card.suit == "♥" or card.suit == "♦":  # colours
                print(f"\033[31m{card}\033[0m")
            else:
                print(f"{card}")

    def deal(self, num_cards):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards left to deal")
        
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]  # removes delt cards
        
        return dealt_cards

    @staticmethod
    def make_deck():
        cards = [] 
        suits = ["♠", "♥", "♣", "♦"]
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

        for suit in suits:  # 4 suits
            for value in values:  # 13 values per suit
                cards.append(Card(suit, value))
                
        return cards

cards = Deck.make_deck()
deck = Deck(cards)
delt_cards = deck.deal(4)
for card in delt_cards:
    print("delt_card:", card)
deck.show_all()