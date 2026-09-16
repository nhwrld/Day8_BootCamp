#task1.1
'''
import pyjokes

print(pyjokes.get_joke("en", "chuck"))
'''

#task2.1
'''
import time
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
'''

#task2.2
'''
import turtle
toto = turtle.Screen()
toto.bgcolor("black")
titi = turtle.Turtle()
titi.color("red")
for i in range(3):
    titi.right(90)
    titi.circle(42)
toto.exitonclick()
'''

#task2.3
'''
import turtle

def draw_polygons(sides):
    toto = turtle.Screen()
    toto.bgcolor("purple")
    titi = turtle.Turtle()
    titi.color("yellow")
    
    if sides == 3:
        titi.forward(100)
        titi.left(120)
        titi.forward(100)
        titi.left(120)
        titi.forward(100)
        titi.left(120)

    if sides ==4:
        for i in range(4):
            titi.forward(100)
            titi.left(90)
        
       
    if sides == 5:
        for i in range(5):
            titi.forward(100)
            titi.right(72)

    if sides == 6:
        for i in range(6):
            titi.forward(100)
            titi.right(60)
        
        
draw_polygons(6)
'''

#task2.4
'''
import turtle

toto = turtle.Screen()
toto.bgcolor("purple")
titi = turtle.Turtle()
titi.color("yellow")

degres = 0

for i in range(30):
    titi.forward(i * 2)
    titi.left(45)
   '''