import random
import itertools
from card import Suit, Rank, Card

class CardCollection:
    def __init__(self, cards):
        self.cards = cards

    def push(self, card):
        self.cards.append(card)

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return (self.cards == [])

    def deal(self, number):
        return CardCollection([self.pop() for i in range(number)])

    def print_all(self):
        for card in self.cards: print(card.literal)

    def shuffle(self):
        random.shuffle(self.cards)

class StandardDeck(CardCollection):
    def __init__(self):
        super().__init__([Card(suit, rank) for suit in Suit for rank in Rank])
        self.shuffle()

col = CardCollection([Card(Suit.CLUBS, Rank.THREE), Card(Suit.SPADES, Rank.ACE), Card(Suit.DIAMONDS, Rank.FOUR), Card(Suit.CLUBS, Rank.JACK)])
col.print_all()
print()

comb = list(itertools.combinations(col.cards, 2))
for combination in comb:
    CardCollection(combination).print_all()
    print()
