import turtle as trtl


import data
import random as rnd

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

# event handlers

endTurntle.onclick(changeTurn)

wn.listen()

# cardNames = ["king", "queen", "jack", "ace"]
# cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# possibleNames = ["king", "queen", "jack", "ace"]


# player1Hand = []
# player2Hand = []

# turn = False

# while True:
    

    
#     if turn == False:
#         player1Hand.append(card)
#     else:
#         player2Hand.append(card)
#     turn = not turn
#     sleep(1)
#     print(f"Player 1 Hand: {player1Hand}")
#     print(f"Player 2 Hand: {player2Hand}")
    






wn.mainloop()