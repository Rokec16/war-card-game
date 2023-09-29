

CARD_SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

CARD_RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
              'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

CARD_VALUES = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
               'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
               'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}


class Card:

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = CARD_VALUES[rank.lower()]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
