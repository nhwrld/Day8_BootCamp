import turtle

toto = turtle.Screen()
toto.bgcolor("white")
titi = turtle.Turtle()
titi.color("red")

def curve():
    for i  in range(200):
        titi.right(1)
        titi.forward(1)

def heart():
    titi.fillcolor("red")
    titi.left(140)
    titi.forward(113)
    curve()
    titi.left(120)
    curve()
    titi.forward(112)
    titi.end_fill

heart()