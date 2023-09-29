import random

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


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in CARD_SUITS:
            for rank in CARD_RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        return self.all_cards.pop()
