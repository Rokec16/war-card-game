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


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


def main():
    player_one = Player('Player One')
    player_two = Player('Player Two')

    new_deck = Deck()
    new_deck.shuffle_cards()

    for _ in range(len(new_deck.all_cards) // 2):
        player_one.add_cards(new_deck.deal_one_card())
        player_two.add_cards(new_deck.deal_one_card())

    game_on = True
    round_number = 0
    while game_on:
        round_number += 1
        print(f'Round {round_number}')

        if len(player_one.all_cards) == 0:
            print(f'{player_one} is out of cards. {player_two} wins the game!')
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print(f'{player_two} is out of cards. {player_one} wins the game!')
            game_on = False
            break

        player_one_cards = []
        player_one_cards.append(player_one.remove_card())
        player_two_cards = []
        player_two_cards.append(player_two.remove_card())

        players_at_war = True
        while players_at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                players_at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                players_at_war = False
            else:
                print('WAR!')

                if len(player_one.all_cards) < 5:
                    print(f'{player_one} unfit for war.')
                    print(f'{player_two} wins the game!')
                    game_on = False
                    break
                elif len(player_two.all_cards) < 5:
                    print(f'{player_two} unfit for war.')
                    print(f'{player_one} wins the game!')
                    game_on = False
                    break
                else:
                    for _ in range(5):
                        player_one_cards.append(player_one.remove_card())
                        player_two_cards.append(player_two.remove_card())


if __name__ == '__main__':
    main()
