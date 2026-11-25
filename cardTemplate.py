import turtle as trtl

def draw_card(name,value, life_span, card_image, x,y):
    card_turtle = trtl.Turtle()
    card_turtle.speed(0)
    card_turtle.hideturtle()
    card_turtle.shape(card_image)
    card_turtle.penup()
    card_turtle.goto(x, y)
    card_turtle.showturtle()
    return {
        "name": name,
        "value": value,
        "life_span": life_span,
        "card_image": card_image,
        "turtle": card_turtle
    }

