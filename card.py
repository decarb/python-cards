from enum import Enum

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Suit(Enum):
    SPADES = 1
    DIAMONDS = 2
    CLUBS = 3
    HEARTS = 4

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.literal = self.rank.name + ' of ' + self.suit.name
