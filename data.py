import random

import cardTemplate as card
import turtle as trtl

from mainScene import updateStack

# ------------- background images -------------

bgPlay1 = "play1Bg.gif"
bgPlay2 = "play2Bg.gif"
endTurn = "endTurn.gif"
# ------------- card names -------------
cardNames = ["thief", "rocket", "rabbit", "gambler", "val1", "val2", "val3", "val4", "val5", "val6", "val7", "val8", "val9", "val10"]
# ------------- turn info -------------

#1 is player 1, 2 is player 2
playerTurn = 1

turnCounter = 0

p1Hand = []
p2Hand = []
p1Stack = 0
p2Stack = 0

#1 is player 1, 2 is player 2
currentPlayer = 1


currentCard = ""
previousCard = ""


cardStackPosition = (-200, -10)

# ------------ card stats ------------

def getCardStats(name):
    value = 0
    life_span = 0
    card_image = ""

    if name == "thief":
        value = 13
        life_span = 10
        card_image = "thief.png"
    elif name == "rocket":
        value = 12
        life_span = 9
        card_image = "rocket.png"
    elif name == "rabbit":
        value = 11
        life_span = 8
        card_image = "rabbit.png"
    elif name == "gambler":
        value = 1
        life_span = 7
        card_image = "gambler.png"
    elif name == "val1":
        value = 2
        life_span = 6
        card_image = "val1.png"
    elif name == "val2":
        value = 3
        life_span = 5
        card_image = "val2.png"
    elif name == "val3":
        value = 4
        life_span = 4
        card_image = "val3.png"
    elif name == "val4":
        value = 5
        life_span = 3
        card_image = "val4.png"
    elif name == "val5":
        value = 6
        life_span = 2
        card_image = "val5.png"
    elif name == "val6":
        value = 7
        life_span = 1
        card_image = "val6.png"
    elif name == "val7":
        value = 8
        life_span = 0
        card_image = "val7.png"
    elif name == "val8":
        value = 9
        life_span = -1
        card_image = "val8.png"
    elif name == "val9":
        value = 10
        life_span = -2
        card_image = "val9.png"
    elif name == "val10":
        value = 11
        life_span = -3
        card_image = "val10.png"

    return [value, life_span, card_image]



def cardAbility(card):
    if card[0] == "thief":
       if currentPlayer == 1:
           randomCard = random.choice(cardNames)
           cardToDraw = card.createCard(randomCard)
           p1Hand.append(cardToDraw)
           card.cardToHand(cardToDraw)
           p1Stack += 3
       else:
           randomCard = random.choice(cardNames)
           cardToDraw = card.createCard(randomCard)
           p2Hand.append(cardToDraw)
           card.cardToHand(cardToDraw)
           p2Stack += 3
    elif card[0] == "rocket":
        if currentPlayer == 1:
            p2Stack -= 3
        else:
            p1Stack -= 3
    elif card[0] == "rabbit":
        if currentPlayer == 1:
            p1Stack += 3
        else:
            p2Stack += 3
    elif card[0] == "gambler":
        pass
    else:
        pass
    updateStack()
