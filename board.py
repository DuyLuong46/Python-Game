'''
DO NOT CHANGE THIS FILE!

CSC 201
Programming Project 4--LittleSpiderBoard class

The LittleSpiderBoard class places cards onto the board and manages the movement
of the cards for a version of the little spider solitaire game. The board has eight tableau piles,
one stock pile, and four foundation piles. The foundation piles begin with the two red aces
and two black kings. Each time cards are dealt from the stock, one card is dealt to
each tableau pile.

'''
from graphics2 import *
from card import *
from deck import *

class LittleSpiderBoard:
    
    NUM_TABLEAUS = 8
    NUM_FOUNDATIONS = 4
    STOCK_X = 690
    STOCK_Y = 350
    INITIAL_FOUNDATION_X = 60
    FOUNDATION_Y = 75
    INITIAL_TABLEAU_X = 60
    TABLEAU_Y = 200
    HORZ_TO_NEXT_PILE = 90

    def __init__(self, window):
        '''
        Initializes the eight tableau locations, the stock pile, and
        the four foundation piles with two red aces and two black kings
        in the graphics window
        
        Params:
        window (GraphWin): the window where the eight tableaus, the stock pile
        and the four foundation piles are drawn
        '''
        self.tableau = [[],[],[],[],[],[],[],[]]
        self.foundation = []
             
        self.stock = Deck(False)
        
        stockSpot = Card('cards/0e.gif')
        stockSpot.move(LittleSpiderBoard.STOCK_X, LittleSpiderBoard.STOCK_Y)
        stockSpot.draw(window)      
        
        self.stockCard = Card('cards/0b.gif')
        self.stockCard.move(LittleSpiderBoard.STOCK_X, LittleSpiderBoard.STOCK_Y)
        self.stockCard.draw(window)
        
        self.emptyTableauList = []
        for i in range(LittleSpiderBoard.NUM_TABLEAUS):
            card = Card('cards/0e.gif')
            card.move(LittleSpiderBoard.INITIAL_TABLEAU_X + LittleSpiderBoard.HORZ_TO_NEXT_PILE * i,
                      LittleSpiderBoard.TABLEAU_Y)
            self.emptyTableauList.append(card)
            card.draw(window)

        self.stock.moveToDealNext(Card('cards/13s.gif'))
        self.stock.moveToDealNext(Card('cards/13c.gif'))
        self.stock.moveToDealNext(Card('cards/1h.gif'))
        self.stock.moveToDealNext(Card('cards/1d.gif'))

        for i in range(LittleSpiderBoard.NUM_FOUNDATIONS):
            self.foundation.append(self.stock.dealCard())

        for i in range(LittleSpiderBoard.NUM_FOUNDATIONS):
            self.foundation[i].move(LittleSpiderBoard.INITIAL_FOUNDATION_X + LittleSpiderBoard.HORZ_TO_NEXT_PILE * i,
                      LittleSpiderBoard.FOUNDATION_Y)
            self.foundation[i].draw(window)
        
    def dealFromStock(self, window):
        '''
        Deals eight cards from the stock pile, one to the top of each tableau
        
        Params:
        window (GraphWin): the window where the eight tableaus, the stock pile
        and the four foundation piles are drawn
        '''
        if not self.stock.isEmpty():
            for i in range(LittleSpiderBoard.NUM_TABLEAUS):
                card = self.stock.dealCard()
                card.move(LittleSpiderBoard.INITIAL_TABLEAU_X + LittleSpiderBoard.HORZ_TO_NEXT_PILE * i,
                          LittleSpiderBoard.TABLEAU_Y)
                self.tableau[i].append(card)
                card.draw(window)
            if self.stock.isEmpty():
                self.stockCard.undraw()      
        
    
    def isPointInFoundationCard(self, point):
        '''
        Checks to see if the point received is in a foundation card
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in an foundation card, False if not.
        '''
        for card in self.foundation:
            if card.containsPoint(point):
                return True
        return False
    
    def isPointInTableauCard(self, point):
        '''
        Checks to see if the point received is in a tableau card
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in an tableau card, False if not.
        '''
        for pile in self.tableau:
            if len(pile) > 0 and pile[-1].containsPoint(point):
                return True
        return False
    
    def isPointInEmptyTableau(self, point):
        '''
        Checks to see if the point received is in an empty tableau
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in an empty tableau, False if not.
        '''
        for i in range(LittleSpiderBoard.NUM_TABLEAUS):
            if len(self.tableau[i]) == 0 and self.emptyTableauList[i].containsPoint(point):
                return True
        return False
    
    def isPointInStockCard(self, point):
        '''
        Checks to see if the point received is in the stock pile
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in the stock pile, False if not.
        '''
        return self.stockCard.containsPoint(point)


    def isStockEmpty(self):
        '''
        Determines if the stock pile is empty or not
        
        Returns:
        True if the stock pile has no cards left; False otherwise
        '''
        return self.stock.getNumCardsLeft() == 0

    def moveCardToFoundationPile(self, card, point, window):
        '''
        Moves the card received to the foundation pile containing the point.
        Note: the move must have been determined valid before using this method
        
        Params:
        card (Card): the card to be moved to the foundation pile
        point (Point): the point in a foundation pile
        window (GraphWin): the window where the four tableaus, the stock pile
        and the foundation piles are drawn
        
        '''
        # find which foundation pile the card is moving to
        foundationIndex = 0
        for i in range(1,LittleSpiderBoard.NUM_FOUNDATIONS):
            if self.foundation[i].containsPoint(point):
                foundationIndex = i

        # find the tableau pile with the card and remove it
        # move the card to the correct foundation pile
        for i in range(0, LittleSpiderBoard.NUM_TABLEAUS):
            if len(self.tableau[i]) > 0 and self.tableau[i][-1] == card:
                self.tableau[i].remove(card)
                card.undraw()
                foundationX = LittleSpiderBoard.INITIAL_FOUNDATION_X + LittleSpiderBoard.HORZ_TO_NEXT_PILE * foundationIndex
                tableauX = LittleSpiderBoard.INITIAL_TABLEAU_X + LittleSpiderBoard.HORZ_TO_NEXT_PILE * i
                card.move(foundationX - tableauX, LittleSpiderBoard.FOUNDATION_Y - LittleSpiderBoard.TABLEAU_Y)
                self.foundation[foundationIndex] = card
                card.draw(window)

                    
    def moveCardToAnotherTableauPile(self, card, point, window):
        '''
        Moves the card received to the tableau containing the point.
        Note: the move must have been determined valid before using this method
        
        Params:
        card (Card): the card to be moved to the tableau pile containing point
        point (Point): the point in a tableau pile
        window (GraphWin): the window where the four tableaus, the stock pile
        and the foundation piles are drawn
        
        '''
        # find the destination tableau pile from the click
        for i in range(0,LittleSpiderBoard.NUM_TABLEAUS):
            if self.emptyTableauList[i].containsPoint(point):
                destinationIndex = i
        
        # move the card to from its current tableau pile to its destination pile
        for i in range(0, LittleSpiderBoard.NUM_TABLEAUS):
            if len(self.tableau[i]) > 0 and self.tableau[i][-1] == card:
                self.tableau[i].remove(card)
                card.undraw()
                destinationX = LittleSpiderBoard.INITIAL_TABLEAU_X + LittleSpiderBoard.HORZ_TO_NEXT_PILE * destinationIndex
                tableauX = LittleSpiderBoard.INITIAL_TABLEAU_X + LittleSpiderBoard.HORZ_TO_NEXT_PILE * i
                card.move(destinationX - tableauX, 0)
                card.draw(window)
                self.tableau[destinationIndex].append(card)
                break
        
   
 

    def getCardAtPoint(self, point):
        '''
        If the point is in some card on the board, that card is returned.
        If the point isn't in a card, then None is returned.
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        If the point is in a card on the board, the card is returned.
        If the point is not in any card on the board, None is returned.
        '''
        for card in self.foundation:
            if card.containsPoint(point):
                return card
        
        for pile in self.tableau:
            if len(pile) > 0 and pile[-1].containsPoint(point):
                return pile[-1]
        return None

     
    def isWin(self):
        '''
        Determines if the board is in a winning state
        
        Returns:
        True if the board is in a winning state; Otherwise return false;
        '''
        if not self.stock.isEmpty():
            return False
        for pile in self.tableau:
            if len(pile) != 0:
                return False
        return True
