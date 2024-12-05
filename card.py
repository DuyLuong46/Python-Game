'''
Name: Duy Luong
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card from a poker deck. Each Card has an image, rank, and suit.
The card stores its position in a graphics window. It can be drawn and undrawn, moved a distance
in the x or y directions, and determine if a point is within the boundaries of the card.

Document Assistance (who and what or declare no assistance):
No assistance


'''
from graphics2 import *
import time

class Card:
    def __init__(self, imageFileName):
        self.imageFileName = imageFileName
        
        rankStartIndex = imageFileName.find('/') + 1
        rankEndIndex = imageFileName.find('.') - 1
        rank = int(imageFileName[rankStartIndex:rankEndIndex])
        self.rank = rank
        
        suitIndex = imageFileName.find('.')
        suit = imageFileName[suitIndex-1]
        self.suit = suit
        
        image = Image(Point(0,0), imageFileName)
        self.image = image

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getImage(self):
        return f"Image(Point(0.0, 0.0), {self.image.getWidth()}, {self.image.getHeight()})"

    def draw(self, window):
        self.image.draw(window)

    def undraw(self):
        self.image.undraw()

    def isRed(self):
        return self.suit in ['h', 'd']

    def move(self, dx, dy):
        self.image.move(dx, dy) 

    def containsPoint(self, point):
        current_position = self.image.getAnchor()
        return (current_position.getX() - self.image.getWidth() / 2 <= point.getX() <= current_position.getX() + self.image.getWidth() / 2 and
                current_position.getY() - self.image.getHeight() / 2 <= point.getY() <= current_position.getY() + self.image.getHeight() / 2)
    
    def __eq__(self, cardToCompare):
        '''
        Allows users of the Card class to compare two cards using ==
        
        Params:
            cardToCompare (Card): the Card to check for equality with this Card
        
        Returns:
            True if the two cards have the same rank and suit. Otherwise, False
        '''
        return self.suit == cardToCompare.suit and self.rank == cardToCompare.rank

    def __str__(self):
        center = self.image.getAnchor()
        return f'suit = {self.suit}, rank = {self.rank}, center = Point({center.getX()}, {center.getY()})'


def main():  
    window = GraphWin("Card Class Testing", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)  # Expected: suit = h, rank = 13, center = Point(0.0, 0.0)
    print(card.getRank())  # Expected: 13
    if (isinstance(card.getRank(), int)):
        print('Rank stored as an int')  # Expected output
    else:
        print('Rank was not stored as an int. Fix it!')
    print(card.getSuit())  # Expected: h
    print(card.getImage())  # Expected to show Image description
    print(card.isRed())  # Expected: True
    
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click only on the card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click only on the card should move it 200 pixels right and 100 pixels down
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 100)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Spades card
    fileName = 'cards/2s.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())  # Expected: 2
    print(card2.getSuit())  # Expected: s
    print(card2.isRed())  # Expected: False
    
    # move card2 to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        