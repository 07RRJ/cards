from dataclasses import dataclass
from random import randint

@dataclass
class Card():
    def make_deck():
        suits = ["♠", "♥", "♣", "♦"]
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        cards = []

        for suit in suits:   # 4 suits
            for value in values: # 13 values per suit
                if suit == "♥" or suit == "♦":
                    cards.append(f"\033[31m{suit} {value}\033[0m")
                else:
                    cards.append(f"{suit} {value}")

        return cards

cards = Card.make_deck()
for card in cards:
    print(card)

