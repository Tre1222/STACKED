import turtle as trtl

import data



def cardToHand(card):
    pass


def createCard(name):
    card_stats = data.getCardStats(name)
    value = card_stats[0]
    life_span = card_stats[1]
    card_image = card_stats[2]

    card = trtl.Turtle()
    card.hideturtle()
    card.shape(card_image)
    card.penup()
    card.goto(data.cardStackPosition)
    card.showturtle()



    return [value, life_span, card_image]




    

def playCard(card, x, y):

    if card[0] == "king":
        pass
    elif card[0] == "queen":
        pass
    elif card[0] == "jack":
        pass
    elif card[0] == "ace":
        pass