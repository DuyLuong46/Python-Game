'''
DO NOT CHANGE THIS FILE!

CSC 201
Programming Project 4--Deck class

The Deck class represents a stadard deck of playing cards with or without two jokers.
The card files for the graphic of each card are in a folder named cards. Each card
file is named with its rank and a letter for its suit. For example, the 4 of hearts
is in the file 4h.gif while the jack of clubs is in the file 11c.gif.

'''
from card import Card
import random

class Deck:
    ACE_LOW = 1
    KING_HIGH = 13
    
    def __init__(self, useJokers = False):
        '''
        Initializes a standard deck of poker cards with ace low and king high.
        Jokers will be included or excluded depending on the parameter received.
        
        Params:
            useJokers (bool): when True Jokers are added to the deck.
        '''
        self.cardList = []
        for rank in range(Deck.ACE_LOW, Deck.KING_HIGH + 1):
            for suit in 'chsd':
                fileName = 'cards/'+ str(rank) + suit + '.gif'
                self.cardList.append(Card(fileName))
        if useJokers:
            self.cardList.append(Card('cards/0j.gif'))
            self.cardList.append(Card('cards/0j.gif'))
        self.currentIndex = 0
        self.shuffle()
    
    def getFullDeckSize(self):
        '''
        Provides access to the number of cards in the full deck.
        
        Returns:
            The number of cards in the full deck
        '''
        return len(self.cardList)
    
    def shuffle(self):
        '''
        Shuffles the cards in the deck and restarts dealing with the first card
        '''
        random.shuffle(self.cardList)
        self.currentIndex = 0
    
    def dealCard(self):
        '''
        Deals the top card from the deck
        '''
        card = self.cardList[self.currentIndex]
        self.currentIndex = self.currentIndex + 1
        return card
    
    def isEmpty(self):
        '''
        Returns True when all cards from the deck have been dealt
        
        Returns:
            bool: True if all of the cards from the deck have been dealt
        '''
        if self.currentIndex == len(self.cardList):
            return True
        else:
            return False
    
    def getNumCardsLeft(self):
        '''
        Provides access to the number of cards still in the deck to deal
        
        Returns:
            The number of cards still in the deck to deal
        '''
        return len(self.cardList) - self.currentIndex
    
    def moveToDealNext(self, cardToMove):
        '''
        Move a card from its location in the deck so that it will now be the next card dealt
        
        Params:
            cardToMove (Card): the card that will be moved to the top of the deck
        '''
        index = self.cardList.index(cardToMove)
        if index < self.currentIndex:
            return False
        else:
            self.cardList.pop(index)
            self.cardList.insert(self.currentIndex, cardToMove)
            return True
    
   
    def __str__(self):
        '''
        Returns a listing of all cards in the deck in the order they will be dealt
        
        Returns:
            str: a listing of all cards in the deck in the order they will be dealt
        '''
        result = ''
        for card in self.cardList:
            result = result + str(card) + '\n'
        return result

        