import random


class Card():
    def __init__(self, color, value, figure):
        self.color = color
        self.value = value
        self.figure = figure


colors = ['Diamond', 'Club', 'Spades', 'Hearth']
deck = []


def generate_deck():
    for color in colors:
        for number in range(2, 15):
            figure = ''
            value = number
            if number == 11:
                figure = 'Jack'
                value = 2
            if number == 12:
                figure = 'Queen'
                value = 3
            if number == 13:
                figure = 'King'
                value = 4
            if number == 14:
                figure = 'Ace'
                value = 11
            if number <= 10:
                figure = str(number)
                value = number
            deck.append(Card(color=color, value=value, figure=figure))
    return deck

generate_deck()
random.shuffle(deck)
player_hand = []
dealer_hand = []

print('~~~~~~WELCOME IN OCZKO THE GAME!~~~~~~')
game_start_or_not = input('Do you want start a game?(Y/N):')

def game():
    print('Lets do this!')
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    started_player_value = player_hand[0].value + player_hand[1].value
    started_dealer_value = dealer_hand[0].value + dealer_hand[1].value
    print('Dealer get:',dealer_hand[0].color,dealer_hand[0].figure)
    print('Value of this cards is:',dealer_hand[0].value)
    print('\n')
    #print('You draw:', player_hand[0].color,player_hand[0].figure,player_hand[1].color,player_hand[1].figure)
    print('Value of your cards is:',sum(player_hand.value))
    player_decision = input('What do you want do with this? [H]it, [S]tay or [Q]uit?')
    if player_decision == 'h':
        hit()
    elif player_decision == 's':
        print('Its dealer turn!')
        print(dealer_hand[0].color, dealer_hand[0].figure,dealer_hand[1].color,dealer_hand[1].figure)
        print('Dealer have',started_dealer_value,'points')
    elif player_decision == 'q':
        exit()

def sum_points(player_hand):
    if







def new_game():
    if game_start_or_not == 'y':
            game()
    elif game_start_or_not == 'n':
        print('OK BYE!')
        exit()


def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        player_hand = []
        dealer_hand = []
        game()
    else:
        print("Bye!")
        exit()


def hit():
    new_card = deck.pop()
    player_hand.append(new_card)
    return player_hand


new_game()
