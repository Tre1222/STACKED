import turtle as trtl


import data
import cardTemplate as card
import random as rnd

# variables




# prepare screen

wn = trtl.Screen()
wn.setup(width=0.85, height=1.0)

# prepare custom images
wn.addshape(data.bgPlay1)
wn.addshape(data.bgPlay2)
wn.addshape(data.endTurn)

# create scene maker turtle

sceneTurtle = trtl.Turtle()
sceneTurtle.speed(0)
sceneTurtle.shape(data.bgPlay1)
sceneTurtle.penup()
sceneTurtle.goto(0, 150)

# create end turn turtle

endTurntle = trtl.Turtle()
endTurntle.speed(0)
endTurntle.shape(data.endTurn)
endTurntle.penup()
endTurntle.goto(600, 0)

# create black screen loading turtle

# create necassaary functions

def changeTurn(x,y):
  if data.playerTurn == 1:
    data.playerTurn = 2
    sceneTurtle.shape(data.bgPlay2)
  else:
    data.playerTurn = 1
    sceneTurtle.shape(data.bgPlay1)
  if data.currentPlayer == 1:
    data.currentPlayer = 2
  else:
    data.currentPlayer = 1

def drawCard(x,y):
    cardName = rnd.choice(data.cardNames)
    cardToDraw = card.createCard(cardName)
    card.cardToHand(cardToDraw)

# event handlers

endTurntle.onclick(changeTurn)
sceneTurtle.onclick(drawCard)
wn.listen()


wn.mainloop()