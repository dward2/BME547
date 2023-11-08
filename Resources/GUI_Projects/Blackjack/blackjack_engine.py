import random
from typing import Union

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
         "King"]


class Card:

    def __init__(self, rank: str, suit: str):
        self.rank: str = rank
        self.suit: str = suit
        try:
            rank_value = int(self.rank)
        except ValueError:
            if self.rank == "Ace":
                rank_value = 1
            else:
                rank_value = 10
        self.rank_value: int = rank_value

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:

    def __init__(self):
        self._deck = []
        for suit in SUITS:
            for rank in RANKS:
                self._deck.append(Card(rank, suit))
        self._discards = []

    def __repr__(self):
        return "Deck: fresh {} discard {}".format(len(self._deck),
                                                  len(self._discards))

    def deal_card(self) -> Card:
        if len(self._deck) == 0:
            raise RuntimeError("Deck out of cards")
        return self._deck.pop(random.randrange(0, len(self._deck)))

    def receive_discard(self, card: Union[Card, list[Card]]) -> None:
        if type(card) not in [Card, list]:
            raise TypeError("Argument not a Card type")
        if type(card) is Card:
            self._discards.append(card)
        else:
            for c in card:
                if type(c) is not Card:
                    raise TypeError("An item in list was not a Card type")
            self._discards.extend(card)

    def reset(self) -> None:
        self.__init__()


class Player:

    def __init__(self, number: int):
        self.number: int = number
        self._cards: list[Card] = []

    def __repr__(self):
        return "Player {} Score: {}".format(self.number, self.score)

    def receive_card(self, card: Card) -> None:
        if type(card) is not Card:
            raise TypeError("Argument not a Card")
        self._cards.append(card)

    def discard_cards(self) -> list[Card]:
        result = self._cards.copy()
        self._cards.clear()
        return result

    def output(self) -> str:
        out_str = "Player {} ".format(self.number)
        out_str += " Score={} ".format(self.score)
        out_str += "Cards={}".format(self._cards)
        return out_str

    @property
    def score(self) -> int:
        found_ace = False
        total = 0
        for card in self._cards:
            total += card.rank_value
            if card.rank_value == 1:
                found_ace = True
        result = total
        if found_ace:
            if (total + 10) <= 21:
                result = total + 10
        return result

    @property
    def cards(self) -> list[str]:
        return [c.__repr__() for c in self._cards]


class Blackjack:

    def __init__(self):
        random.seed()
        self._deck = Deck()
        self._player = Player(0)
        self._dealer = Player(1)
        self._initial_deal()

    def _initial_deal(self):
        for i in range(2):
            self.deal_card_to_player()
            self.deal_card_to_dealer()

    def deal_card_to_player(self) -> str:
        card = self._deck.deal_card()
        self._player.receive_card(card)
        return card.__repr__()

    def deal_card_to_dealer(self) -> str:
        card = self._deck.deal_card()
        self._dealer.receive_card(card)
        return card.__repr__()

    def new_round_reshuffle(self) -> None:
        self._player.discard_cards()
        self._dealer.discard_cards()
        self._deck.reset()
        self._initial_deal()

    @property
    def player_score(self) -> int:
        return self._player.score

    @property
    def dealer_score(self) -> int:
        return self._dealer.score

    @property
    def dealer_cards(self) -> list[str]:
        return self._dealer.cards

    @property
    def player_cards(self) -> list[str]:
        return self._player.cards
