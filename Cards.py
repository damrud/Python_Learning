
class Card:
    def __init__(self, figure, color):
        self.figures = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.figure = self.figures[figure]
        self.colors = {"D": "Diamond", "C": "Club", "H": "Hearth", "S": "Spades"}
        self.color = self.colors[color]
        self.value = -1
