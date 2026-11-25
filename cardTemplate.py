import turtle as trtl

class Card:
    def __init__(
            self,
            card_image,
            card_type,
            card_value,
            life_span):
        # Instance attributes (unique to each card)
        self.cardImage = card_image
        self.cardValue = card_value   # 1-9 normal cards, -5 to 0 special cards
        self.lifeSpan = life_span     # How many turns this card can exist
        self.turtle = trtl.Turtle()   # Gives each card its own turtle to draw itself

    def onDrawCard(self, x, y):
        pass

    def onPlaceCard(self):
        pass