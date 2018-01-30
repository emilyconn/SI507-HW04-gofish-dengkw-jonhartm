import random

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
            if rank in self.face_cards:
                self.rank = self.face_cards[rank]
            else:
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

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    # draw a card from deck
    # input: None
    # output: a card
    def pop_card(self):
        return self.cards.pop()

    # add the cards to the deck when someone show and remove the same
    # four cards
    # input: list of cards
    # output: None
    def add_cards(self, cards):
        self.cards.append(cards)

    # shuffle the deck, after initializing a new deck and add the four same cards
    # input: None
    # output: None
    def shuffle(self):
        random.shuffle(self.cards)


class Hand:

    def __init__(self, init_cards):

        if not isinstance(init_cards, list):
            raise TypeError("Input should be a list of cards")

        self.cards = init_cards

    def __str__(self):
        total = []
        for card in self.cards:
            total.append(card.__str__())
        # shows up in whatever order the cards are in
        return "\n".join(total)

    # show the ranks of cards in one players hand
    # input: None
    # output: a list of ranks
    def get_rank(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        return ranks

    # add cards from another player
    # input: a card
    # output: None
    def add_card(self, card):
        if str(card) not in [str(c) for c in self.cards]:
            self.cards.append(card)

    # when requested by another player, remove the card with that rank
    # this card will be the input of add_card
    # input: rank (2 ~ 10, Ace, Jack, Queen, King)
    # output: a card
    def remove_card(self, rank):
        index_to_remove = self.get_rank().index(rank)
        return self.cards.pop(index_to_remove)

    # draw a card from deck
    # input: deck
    # output: None
    def draw_card(self, deck):
        self.add_card(deck.pop_card())

    # Judge if the deck have four same rank
    # if True, output: True, and the rank
    # if False, output: False, and None
    def isFour(self):
        ranks = self.get_rank()
        rank_count = {}
        for r in ranks:
            rank_count[r] = rank_count.get(r, 0) + 1
        if 4 in rank_count.values():
            return True, [k for k, v in rank_count.items if v == 4][0]
        else:
            return False, None

    # remove the four same rank cards from hand
    # input: rank
    # output: a list of cards with same rank
    def remove_four(self, rank):
        self.cards = [card for card in self.cards if card.rank != rank]
        return [card for card in self.cards if card.rank == rank]

if __name__ == '__main__':
    print("Game Start!")
    deck = Deck()
    deck.shuffle()
    player1 = Hand([])
    player2 = Hand([])
    for i in range(7):
        player1.draw_card(deck)
        player2.draw_card(deck)
