from card_collection import CardCollection
from card import Suit, Rank, Card

class StandardDeck(CardCollection):
    def __init__(self):
        super().__init__([Card(suit, rank) for suit in Suit for rank in Rank])
        self.shuffle()

d = StandardDeck()
d.print_all()
