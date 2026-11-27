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
wn.addshape("cardVal1NoBg.gif")
wn.addshape("cardVal2NoBg.gif")
wn.addshape("cardVal3NoBg.gif")
wn.addshape("cardVal4NoBg.gif")
wn.addshape("cardVal5NoBg.gif")
wn.addshape("cardVal6NoBg.gif")
wn.addshape("cardVal7NoBg.gif")
wn.addshape("cardVal8NoBg.gif")
wn.addshape("cardVal9NoBg.gif")
wn.addshape("cardVal10NoBg.gif")
wn.addshape("cardTheif.gif")
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

player1StackTurtle = trtl.Turtle()
player1StackTurtle.speed(0)
player1StackTurtle.penup()
player1StackTurtle.goto(-200, -10)

player2StackTurtle = trtl.Turtle()
player2StackTurtle.speed(0)
player2StackTurtle.penup()
player2StackTurtle.goto(200, -10)

# create black screen loading turtle

# create necassaary functions
def updateStack():
    player1StackTurtle.clear()
    player2StackTurtle.clear()
    player1StackTurtle.write(f"Player 1 Stack: {data.p1Stack}", font=("Arial", 16, "normal"))
    player2StackTurtle.write(f"Player 2 Stack: {data.p2Stack}", font=("Arial", 16, "normal"))


def changeTurn(x,y):
  if data.playerTurn == 1:
    data.playerTurn = 2
    sceneTurtle.shape(data.bgPlay2)
  else:
    data.playerTurn = 1
    sceneTurtle.shape(data.bgPlay1)
  if data.currentPlayer == 1:
    data.currentPlayer = 2
  elif data.currentPlayer == 2:
    data.currentPlayer = 1

  if data.currentPlayer == 1:
     for card in data.p2Hand:
        card[3].hideturtle()
     for card in data.p1Hand:
        card[3].showturtle()
  elif data.currentPlayer == 2:
     for card in data.p2Hand:
        card[3].showturtle()
     for card in data.p1Hand:
        card[3].hideturtle()
  
  data.turnTaken = False
  
def drawCard(x,y):
    if data.turnTaken:
        return
    data.turnTaken = True
    cardName = rnd.choice(data.cardNames)
    cardToDraw = card.createCard(cardName)
    card.cardToHand(cardToDraw)

# event handlers

endTurntle.onclick(changeTurn)
sceneTurtle.onclick(drawCard)
wn.listen()


wn.mainloop()