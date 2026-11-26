import turtle as trtl

import data



def cardToHand(card):
    if data.currentPlayer == 1:
        
        data.p1Hand.append(card)
        if len(data.p1Hand) % 2 == 0:
            card[3].goto(-10 * len(data.p1Hand), -200)
        else:
            card[3].goto(10 * len(data.p1Hand), -200)
    
    elif data.currentPlayer == 2:
        
        data.p2Hand.append(card)
        if len(data.p2Hand) % 2 == 0:
            card[3].goto(-10 * len(data.p2Hand), -200)
        else:
            card[3].goto(10 * len(data.p2Hand), -200)
    



def cardToStack(card):
    card[3].goto(data.cardStackPosition)

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



    return [value, life_span, card_image, card]




    

def playCard(card, x, y):

    if card[0] == "thief":
        pass
    elif card[0] == "rocket":
        pass
    elif card[0] == "jack":
        pass
    elif card[0] == "gambler":
        pass