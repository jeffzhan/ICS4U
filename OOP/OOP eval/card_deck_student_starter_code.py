import random


class Card:

    _valueDictionary = {'A':1, 'J':11, 'Q':12, 'K':13}
    
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    def value(self):

        if self._value in Card._valueDictionary:
            return Card._valueDictionary[self._value]
        else:
            return self._value

    def suit(self):
        return self._suit


    def __eq__(self, otherCard):

        return self.value() == otherCard.value() and self.suit() == otherCard.suit()
    

    def __lt__(self, otherCard):

        return self.value() < otherCard.value()
            

    def __gt__(self, otherCard):

        return self.value() > otherCard.value()

    def __str__(self):
        return f'{self._value} of {self._suit}'

    def __repr__(self):
        return f'class Card(value={self._value}, suit={self._suit})'




class Deck:

    _numCards = 52
    _cardValues = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    _suits = ['hearts', 'spades', 'clubs', 'diamonds']

    def __init__(self):

        self._cards = self._generateCards()

    @classmethod
    def _generateCards(cls):

        d = []
        for s in cls._suits:
            for v in cls._cardValues:
                d.append(Card(v, s))
        return d

    def __getitem__(self, key):

        return self._cards[key]

    def __str__(self):
        s = ""
        for c in self._cards:
            s += c.__str__() + "\n"

        return s

    def shuffle(self):

        for i in range(0, 10):
            random.shuffle(self._cards)

    def __len__(self):
        return len(self._cards)

    def empty(self):
        return len(self._cards) == 0

    def deal(self):
        return self._cards.pop(0)




class Canasta(Deck):

    def __init__(self):
        self._cards = 3 * self._generateCards()
        
        for i in range(6):
            self._cards.append(Card(0, 'joker'))



class Euchre(Deck):

    def __init__(self):
        self._cards = self._generateCards()
        
        card_list = []

        for card in self._cards:
            if not (2 <= card.value() <= 8):
                card_list.append(card)
        self._cards = card_list

                

class BlackJack(Deck):

    def __init__(self):
        self._cards = 8 * self._generateCards()
        self.shuffle()
