import turtle as trtl

#1 is player 1, 2 is player 2
currentTurn = 1

p1Hand = []
p2Hand = []

currentCard = ""
previousCard = ""


cardStackPosition = (-200, -10)


def getCardStats(name):
    value = 0
    life_span = 0
    card_image = ""

    if name == "king":
        value = 13
        life_span = 10
        card_image = "king.png"
    elif name == "queen":
        value = 12
        life_span = 9
        card_image = "queen.png"
    elif name == "jack":
        value = 11
        life_span = 8
        card_image = "jack.png"
    elif name == "ace":
        value = 1
        life_span = 7
        card_image = "ace.png"
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





