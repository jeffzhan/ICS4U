import random

class Card:

    _valueDictionary = {'A': 1, 'J':11, 'Q':12, 'K':13}
    
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

    def __repr__(self):
        return f'class Card(value={self._value}, suit={self._suit})'


    def __eq__(self, otherCard):

        return self.value() == otherCard.value() and self.suit() == otherCard.suit()
    

    

class Deck:

    _numCards = 52
    _cardValues = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    _suits = ['hearts', 'spades', 'clubs', 'spades']

    def __init__(self):

        self._cards = self._generateCards()


    @classmethod
    def _generateCards(self):

        d = []
        for s in Deck._suits:
            for v in Deck._cardValues:
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
        pass


    def __len__(self):
        pass
        
    def empty(self):
        pass

    def deal(self):
        pass
        


class Hand(Deck):

    pass


    

    
            
        

def game():

    

    input("Press any key to continue")

        
            

game()       
    
        
        
