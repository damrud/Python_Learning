from Cards import Card
import random

def getFigure(self):
    return self.figure

def getColor(self):
    return self.color

def cardValue(self):
    if self.figure == "Ace":
        cardValue = 11
    elif self.figure == "Jack":
        cardValue = 2
    elif self.figure == "Queen":
        cardValue == 3
    elif sel.figure == "King":
        cardValue = 4
    elif type(self.figure) is int:
        if self.rank < 11:
            self.figure = self.figures[self.figure]
    return self.value
