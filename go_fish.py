class Card():
    suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    face_cards = {1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}

    def __init__(self, suit=0, rank=1):
        # check for integer values for suit and rank
        if not isinstance(suit, int) or not isinstance(rank, int):
            raise TypeError("Suit and Rank must be integers")

        # check for valid suit
        if suit >= 0 and suit <=4:
            self.suit = self.suits[suit]
        else:
            raise IndexError("Suit must be between 0 and 3")

        #check for valid rank
        if rank >= 1 and rank <= 13:
            self.rank = rank
        else:
            raise IndexError("Rank must be between 1 and 13")

    def __str__(self):
        # check to see if it's a face card
        if self.rank in self.face_cards:
            return "The {} of {}".format(self.face_cards[self.rank], self.suit)
        else:
            return "The {} of {}".format(self.rank, self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
