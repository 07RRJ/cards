#skapa en kortlek med hjälp av objektorienterad programmering - använd klasser. Läs mer på classroom - uppgift4.

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        pass


class Deck:
    def __init__(self, cards=None): 
        if cards is None:
            cards = []
        self.cards = cards
        
        
        